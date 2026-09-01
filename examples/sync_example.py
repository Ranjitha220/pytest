from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://example.com")
        print(page.title())

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
