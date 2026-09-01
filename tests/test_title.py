import pytest


@pytest.mark.smoke
def test_title(page, app_config):
    page.goto(app_config.base_url)
    page_title = page.title()
    assert page_title == "Example Domain"