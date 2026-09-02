import pytest

CORPORATE_URL = "/corporate"

@pytest.mark.smoke

def test_corporate_url(page, app_config):
    page.goto(app_config.base_url + CORPORATE_URL)
    page_title = page.title()
    assert page_title == "Akbar Travels - Best Travel Website. Book Flights, Hotels, Holidays & more"
