from pathlib import Path
from playwright.sync_api import sync_playwright
import pytest
import pytest_html
import shutil
import os
import base64
import re
import json

from config import BASE_URL

VIDEO_DIR = Path("videos")
RECORDINGS_DIR = Path("recordings")
SCREENSHOTS_DIR = Path("screenshots")


@pytest.fixture(scope="session")
def browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    yield browser
    try:
        browser.close()
    except Exception:
        pass
    try:
        p.stop()
    except Exception:
        pass


@pytest.fixture(scope="function")
def page(browser, request):
    VIDEO_DIR.mkdir(exist_ok=True)
    RECORDINGS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    # use a test-specific subdirectory so we can reliably find the recorded file
    test_video_dir = VIDEO_DIR / request.node.name
    test_video_dir.mkdir(exist_ok=True)

    context = browser.new_context(ignore_https_errors=True, record_video_dir=str(test_video_dir))
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    yield page

    # close context to finalize the video
    try:
        context.close()
    except Exception:
        pass

    # move the produced webm to recordings with a stable name
    try:
        # collect candidate webm files under the test video dir or the top-level VIDEO_DIR
        candidates = list(test_video_dir.glob("*.webm"))
        candidates += [f for f in VIDEO_DIR.glob("page@*.webm")]

        # if none found under those, search recursively as a last resort
        if not candidates:
            candidates = list(VIDEO_DIR.rglob("*.webm"))

        if candidates:
            # pick the newest file (most likely the current test's video)
            src = max(candidates, key=lambda p: p.stat().st_mtime)
            dest = RECORDINGS_DIR / f"{request.node.name}.webm"
            shutil.move(str(src), str(dest))
            # save path on the node for the report hook
            setattr(request.node, "video_path", str(dest))
        else:
            setattr(request.node, "video_path", None)
    except Exception:
        setattr(request.node, "video_path", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # attach the report object to the item so fixtures can inspect it later
    setattr(item, "rep_" + report.when, report)

    extra = getattr(report, "extra", [])

    # capture screenshot on failure (call phase)
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            SCREENSHOTS_DIR.mkdir(exist_ok=True)

            file_name = SCREENSHOTS_DIR / f"{item.name}.png"

            try:
                page.screenshot(path=str(file_name))
                extra.append(pytest_html.extras.image(str(file_name)))
            except Exception:
                pass

    # attach recording (video) in teardown phase
    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)
        if video_path:
            try:
                # embed the video into the report as a base64 data URI so
                # the generated report.html is self-contained and includes the video
                with open(video_path, "rb") as f:
                    data = f.read()
                b64 = base64.b64encode(data).decode("ascii")
                html = (
                    f'<video controls width="640">'
                    f'<source src="data:video/webm;base64,{b64}" type="video/webm">'
                    "Your browser does not support the video tag." "</video>"
                )
                extra.append(pytest_html.extras.html(html))
            except Exception:
                pass

    report.extra = extra


def _embed_videos_into_report(report_path: Path):
    if not report_path.exists():
        return

    content = report_path.read_text(encoding="utf-8")

    # Build a JS mapping from test short-name -> base64 video HTML
    mapping = {}
    for video in RECORDINGS_DIR.glob("*.webm"):
        test_short = video.stem  # e.g., test_social
        try:
            with open(video, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            video_html = (
                f'<div class="injected-video">'
                f'<video controls width="640">'
                f'<source src="data:video/webm;base64,{b64}" type="video/webm">'
                'Your browser does not support the video tag.'
                '</video></div>'
            )
            mapping[test_short] = video_html
        except Exception:
            continue

    if not mapping:
        return

    # Create a JS script that finds rows by testId and injects the video HTML
    # Use conservative DOM queries to avoid touching the report's JSON
    script_lines = ["<script>(function(){var map=", json.dumps(mapping), ";",
                    "function inject(){",
                    "var ids=document.querySelectorAll('.col-testId');",
                    "for(var i=0;i<ids.length;i++){var el=ids[i];var txt=el.textContent||el.innerText;",
                    "for(var k in map){if(txt.indexOf('::'+k)!==-1){",
                    "var row=el.closest('tbody').querySelector('.extras-row .extraHTML');",
                    "if(row){row.innerHTML = map[k] + row.innerHTML;} } } } }",
                    "if(document.readyState==='complete'){inject();}else{window.addEventListener('load',inject);} })();</script>"]

    # append the script before </body>
    insert_at = content.rfind('</body>')
    if insert_at == -1:
        # append at end
        content = content + '\n' + ''.join(script_lines)
    else:
        content = content[:insert_at] + '\n' + ''.join(script_lines) + content[insert_at:]

    report_path.write_text(content, encoding="utf-8")


def pytest_sessionfinish(session, exitstatus):
    # try to find the html report path from config, fallback to report.html
    htmlpath = None
    try:
        htmlpath = getattr(session.config.option, "htmlpath", None)
    except Exception:
        htmlpath = None

    report_file = Path(htmlpath) if htmlpath else Path("report.html")
    _embed_videos_into_report(report_file)


def pytest_html_results_table_html(report, *args, **kwargs):
    """Called by pytest-html to allow adding extra HTML to the results table for a test.
    Different versions of pytest-html expose different hook signatures. Use flexible
    args/kwargs so this hook doesn't fail plugin validation. If an `extra` list is
    available (either as a kwarg, positional arg, or on `report.extra`), append
    the per-test video HTML there.
    """
    try:
        nodeid = getattr(report, 'nodeid', None)
        if not nodeid:
            return

        short = nodeid.split('::')[-1]
        video_file = RECORDINGS_DIR / f"{short}.webm"
        if video_file.exists():
            with open(video_file, 'rb') as f:
                b64 = base64.b64encode(f.read()).decode('ascii')
            html = (
                f'<div class="injected-video">'
                f'<video controls width="640">'
                f'<source src="data:video/webm;base64,{b64}" type="video/webm">'
                'Your browser does not support the video tag.'
                '</video></div>'
            )

            # locate the 'extra' list from kwargs, positional args, or report
            extra = None
            if 'extra' in kwargs:
                extra = kwargs['extra']
            elif len(args) >= 1:
                extra = args[0]
            else:
                extra = getattr(report, 'extra', None)

            if extra is None:
                # ensure report.extra exists and add to it
                cur = getattr(report, 'extra', []) or []
                cur.append(pytest_html.extras.html(html))
                setattr(report, 'extra', cur)
            else:
                extra.append(pytest_html.extras.html(html))
    except Exception:
        return