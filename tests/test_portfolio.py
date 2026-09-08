

import pytest


from pages.portfolio import Portfolio






@pytest.mark.smoke
def test_blogger(page):
    P=Portfolio(page)
    P.portfo()



