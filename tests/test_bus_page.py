import pytest

BUS_URL = "/bus-ticket-booking/"

@pytest.mark.smoke
def test_bus_url(page, app_config):
    page.goto(app_config.base_url + BUS_URL)
    page_title = page.title()
    assert page_title == "Bus Ticket Booking Online at Lowest Price | Akbar Travels"






