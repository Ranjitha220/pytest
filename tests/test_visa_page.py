import pytest

VISA_URL = "/visa"

@pytest.mark.smoke

def test_visa_url(page, app_config):
    page.goto(app_config.base_url + VISA_URL)
    page_title = page.title()
    assert page_title == "Visa Consultants: Tourist Visa & Business Visa Application Services Online | Akbar Travels"
