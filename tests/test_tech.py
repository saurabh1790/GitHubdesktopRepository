

import pytest

from pages.technologies import Technologies




@pytest.mark.smoke
def test_techNav(page):
    T=Technologies(page)
    T.techNav()


@pytest.mark.smoke
def test_techmobiledev(page):
    T=Technologies(page)
    T.techmobile()
