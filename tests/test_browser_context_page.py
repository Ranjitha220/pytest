import pytest

@pytest.mark.regression
def test_browser_context_page(browser, app_config):
    context = browser.new_context()
    page = context.new_page()

    page.goto(app_config.base_url)

    print("\nFinal URL:", page.url)

    assert page.url.startswith(app_config.base_url)

    context.close()