# Python Playwright Starter Framework

## 1. Create virtual environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
```

If browser installation needs OS dependencies on Linux:

```bash
python -m playwright install --with-deps
```

## 3. Environment variables

Copy `.env.example` to `.env` and replace values.

Never commit `.env` or real passwords/tokens.

## 4. Run tests

```bash
pytest
```

Run a specific browser:

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Run headed:

```bash
pytest --headed
```

Run multiple workers:

```bash
pytest -n auto
```

## 5. Sync vs Async API

The example test uses the synchronous pytest-playwright fixtures.

For application code requiring async execution, use:

```python
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()


asyncio.run(main())
```

## 6. Pytest Playwright fixtures

The pytest plugin provides fixtures such as:

- `browser`
- `context`
- `page`

Example:

```python
def test_homepage(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

## 7. Browser matrix

The pytest-playwright plugin supports browser selection with:

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

You can run more than one:

```bash
pytest --browser chromium --browser firefox --browser webkit
```

## 8. Pip errors and dependency conflicts

Recommended troubleshooting:

```bash
python -m pip --version
python -m pip install --upgrade pip setuptools wheel
pip check
pip install -r requirements.txt
python -m playwright install
```

If the virtual environment is corrupted, recreate it rather than modifying the global Python installation.

## 9. Secrets

For local learning, use `.env`.

For CI/CD, prefer the CI platform's secret store instead of putting credentials in source code or `.env` files.

Never do this:

```python
PASSWORD = "MyRealPassword123"
```
