import pytest


@pytest.mark.smoke
def test_homepage(page, app_config):
    page.goto(app_config.base_url)

    print("\nURL:", page.url)
    print("Title:", page.title())

    assert page.title() != ""
    assert page.locator("body").is_visible()
