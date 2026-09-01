import pytest

BUS_URL = "https://www.akbartravels.com/in/bus-ticket-booking/"

@pytest.mark.smoke
def test_bus_url(page):
    page.goto(BUS_URL)
    page_title = page.title()

    print("\nURL:", page.url)
    print("TITLE:", page.title())
    assert page_title == "Bus Ticket Booking Online at Lowest Price | Akbar Travels"



