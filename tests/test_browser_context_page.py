import pytest

@pytest.mark.regression
def test_browser_context_page(browser, app_config):
    context = browser.new_context()
    page = context.new_page()

    page.goto(app_config.base_url)

    assert page.url.startswith(app_config.base_url)

    context.close()