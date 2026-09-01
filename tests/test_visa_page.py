import pytest

VISA_URL = "https://www.akbartravels.com/visa"

@pytest.mark.smoke
def test_visa_url(page):
    page.goto(VISA_URL)
    page_title = page.title()

    print("\nURL:", page.url)
    print("TITLE:", page.title())
    assert page_title == "Visa Consultants: Tourist Visa & Business Visa Application Services Online | Akbar Travels"
