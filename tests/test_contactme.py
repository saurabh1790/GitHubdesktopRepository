import pytest

from pages.contact import Contact

@pytest.mark.smoke
def test_contactme(page):
    C=Contact(page)
    C.contactus()