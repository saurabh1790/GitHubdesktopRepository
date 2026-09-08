

import pytest

from pages.blogs import Blog






@pytest.mark.smoke
def test_blogger(page):
    B=Blog(page)
    B.fblo()



