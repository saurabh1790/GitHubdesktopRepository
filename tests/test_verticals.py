

import pytest

from pages.verticals import V

@pytest.mark.smoke
def test_verticals(page):
    vert=V(page)
    vert.tradingNav()

@pytest.mark.smoke
def test_retailandecommerce(page):
    vert=V(page)
    vert.retailandecommerce()

@pytest.mark.smoke
def test_healthcare(page):
    vert=V(page)
    vert.vhealthcare()

@pytest.mark.smoke
def test_fintech(page):
    vert=V(page)
    vert.fintechh()

@pytest.mark.smoke
def test_customapp(page):
    vert=V(page)
    vert.customapp()
    






