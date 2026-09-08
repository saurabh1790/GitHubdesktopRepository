import pytest

from pages.social import socialmedia



@pytest.mark.smoke
def test_social(page):
    S=socialmedia(page)
    S.socialmediapageclick()