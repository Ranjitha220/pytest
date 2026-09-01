import pytest

CORPORATE_URL = "https://www.akbartravels.com/in/corporate?lan=en"

@pytest.mark.smoke
def test_corporate_url(page):
    page.goto(CORPORATE_URL)
    page_title = page.title()

    print("\nURL:", page.url)
    print("TITLE:", page.title())
    assert page_title == "Akbar Travels - Best Travel Website. Book Flights, Hotels, Holidays & more"



