# Python Playwright — A to Z Beginner Guide

This guide explains the starter framework from absolute beginner level.

The goal is not just to make tests run. The goal is to understand **why each file exists, what each command does, and how Python, Playwright, and pytest work together**.

---

# 1. What are Python, Playwright, and pytest?

Before touching the framework, understand the three main pieces.

## Python

Python is the programming language we use to write our automation.

Example:

```python
name = "John"
print(name)
```

Python executes this code and prints:

```text
John
```

## Playwright

Playwright is a browser automation library.

It can control:

- Chromium / Chrome
- Firefox
- WebKit

It can:

- open a browser
- open a page
- click buttons
- enter text
- select values
- upload files
- read text
- verify elements
- take screenshots
- record traces
- automate complete user journeys

Example:

```python
page.goto("https://example.com")
```

This tells Playwright to navigate the browser to the website.

## pytest

pytest is a Python testing framework.

It gives us:

- test discovery
- assertions
- fixtures
- test markers
- setup and teardown
- parameterization
- reporting
- plugins

Playwright performs browser automation.

pytest organizes and executes the tests.

---

# 2. How everything connects

The basic architecture is:

```text
Python
  |
  +-- pytest
        |
        +-- pytest-playwright
              |
              +-- Playwright
                    |
                    +-- Chromium
                    +-- Firefox
                    +-- WebKit
```

For example:

```text
test_homepage.py
       |
       v
     pytest
       |
       v
pytest-playwright
       |
       v
   Playwright
       |
       v
    Browser
       |
       v
     Website
```

---

# 3. Understanding the project folder

Our project looks like this:

```text
playwright_python_framework/
│
├── .env.example
├── .gitignore
├── README.md
├── EXPLAIN_A_TO_Z.md
├── requirements.txt
├── pytest.ini
├── playwright.config.py
│
├── tests/
│   ├── conftest.py
│   ├── test_homepage.py
│   └── test_browser_context_page.py
│
├── examples/
│   ├── sync_example.py
│   └── async_example.py
│
├── pages/
├── utils/
├── data/
├── logs/
├── reports/
│
└── scripts/
    ├── install.sh
    └── install.ps1
```

Do not worry if this looks complicated.

We will understand every folder one by one.

---

# 4. What is a project folder?

A project folder is simply a directory that contains everything required for our automation project.

For example:

```text
playwright_python_framework/
```

Inside it we keep:

- Python code
- tests
- configuration
- test data
- logs
- reports
- dependencies

Keeping everything inside one project makes the framework easier to manage.

---

# 5. Python virtual environment

## What is a virtual environment?

A virtual environment is an isolated Python environment for a project.

Imagine you have two projects:

```text
Project A
Playwright version X

Project B
Playwright version Y
```

If both projects use the same global Python packages, they can conflict.

A virtual environment separates them.

Think of it as:

```text
Computer
│
├── Global Python
│
├── Project A
│   └── .venv
│
└── Project B
    └── .venv
```

Each project gets its own packages.

---

# 6. Creating a virtual environment

On Windows:

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
python3 -m venv .venv
```

Let's understand the command.

```text
python
```

Runs Python.

```text
-m
```

Means:

> Run a Python module.

```text
venv
```

Python's built-in virtual-environment module.

```text
.venv
```

The folder where the environment will be created.

So:

```bash
python -m venv .venv
```

means:

> Create a Python virtual environment named `.venv`.

---

# 7. Activating the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

After activation, your terminal may look like:

```text
(.venv) C:\project>
```

The `(.venv)` means the virtual environment is active.

---

# 8. Why use `.venv`?

`.venv` is a common convention.

You could call it:

```text
environment
```

or:

```text
myenv
```

But `.venv` is widely recognized by editors such as VS Code.

We normally do not commit `.venv` to Git.

That is why `.gitignore` contains:

```text
.venv/
```

---

# 9. requirements.txt

Open:

```text
requirements.txt
```

We have:

```text
playwright
pytest
pytest-playwright
python-dotenv
pytest-xdist
```

This file tells Python which external packages our project needs.

Think of it as a shopping list.

```text
requirements.txt
        |
        +-- playwright
        +-- pytest
        +-- pytest-playwright
        +-- python-dotenv
        +-- pytest-xdist
```

---

# 10. Installing requirements

Run:

```bash
pip install -r requirements.txt
```

Better:

```bash
python -m pip install -r requirements.txt
```

What does `-r` mean?

It means:

> Read the package requirements from this file.

So:

```bash
pip install -r requirements.txt
```

means:

> Install everything listed in requirements.txt.

---

# 11. What is pip?

`pip` is Python's package installer.

For example:

```bash
pip install pytest
```

means:

> Download and install pytest.

You can think of pip as the package manager for Python.

---

# 12. Upgrade pip

Before installing packages, it is often useful to run:

```bash
python -m pip install --upgrade pip
```

This updates pip itself.

---

# 13. Installing Playwright browsers

Installing the Python package is not enough.

First:

```bash
pip install playwright
```

Then:

```bash
python -m playwright install
```

Why?

Because Playwright needs browser binaries.

Conceptually:

```text
Python package
      +
Browser binaries
      =
Playwright automation
```

---

# 14. Installing Linux dependencies

On supported Linux systems:

```bash
python -m playwright install --with-deps
```

This installs browser dependencies required by the operating system.

---

# 15. Checking installation

You can check Python:

```bash
python --version
```

Check pip:

```bash
python -m pip --version
```

Check Playwright:

```bash
python -m playwright --version
```

Check pytest:

```bash
pytest --version
```

---

# 16. Common pip problems

## Problem: `pip` is not recognized

Try:

```bash
python -m pip --version
```

Using:

```bash
python -m pip
```

is often safer because it makes it clear which Python installation is being used.

---

# 17. Dependency conflicts

Suppose:

```text
Package A requires X version 1
Package B requires X version 2
```

Now Python may report a dependency conflict.

First check:

```bash
pip check
```

You can also inspect installed packages:

```bash
pip list
```

A clean virtual environment is often the easiest solution.

---

# 18. When should you recreate `.venv`?

If the environment becomes badly corrupted:

Windows:

```bash
rmdir /s /q .venv
```

macOS/Linux:

```bash
rm -rf .venv
```

Then recreate:

```bash
python -m venv .venv
```

Activate it and reinstall:

```bash
pip install -r requirements.txt
python -m playwright install
```

Be careful when deleting directories.

---

# 19. Sync vs Async Playwright

Playwright Python provides two APIs.

## Synchronous API

```python
from playwright.sync_api import sync_playwright
```

Example:

```python
with sync_playwright() as p:
    browser = p.chromium.launch()
```

The program waits for each operation to complete.

For beginners, synchronous Playwright is usually easier to understand.

---

# 20. Asynchronous API

```python
from playwright.async_api import async_playwright
```

Example:

```python
async with async_playwright() as p:
    browser = await p.chromium.launch()
```

You will see:

```python
async
```

and:

```python
await
```

Async code is useful when your application or test architecture already uses asynchronous programming.

---

# 21. Sync example explained

Open:

```text
examples/sync_example.py
```

You will see:

```python
from playwright.sync_api import sync_playwright
```

This imports the synchronous Playwright API.

Then:

```python
with sync_playwright() as p:
```

starts Playwright.

`p` represents the Playwright object.

Then:

```python
browser = p.chromium.launch(headless=True)
```

starts Chromium.

---

# 22. What is a browser?

A browser is the actual browser process.

Example:

```python
browser = p.chromium.launch()
```

Conceptually:

```text
Playwright
   |
   v
Browser
```

---

# 23. Browser, Context, Page

This is one of the most important Playwright concepts.

The hierarchy is:

```text
Browser
   |
   +-- Context
          |
          +-- Page
```

Think of a real browser.

```text
Chrome
│
├── User/session 1
│   ├── Tab 1
│   └── Tab 2
│
└── User/session 2
    └── Tab 1
```

In Playwright:

```text
Browser
│
├── BrowserContext
│   ├── Page
│   └── Page
│
└── BrowserContext
    └── Page
```

---

# 24. Browser

Example:

```python
browser = p.chromium.launch()
```

The browser is the browser process.

---

# 25. Browser Context

Create a context:

```python
context = browser.new_context()
```

A context provides an isolated browser session.

It can have its own:

- cookies
- local storage
- session storage
- permissions
- authentication state

This makes contexts extremely useful for testing.

---

# 26. Page

Create a page:

```python
page = context.new_page()
```

A page is essentially a browser tab.

Then:

```python
page.goto("https://example.com")
```

navigates that tab.

---

# 27. Complete browser flow

```python
browser = ...
context = browser.new_context()
page = context.new_page()

page.goto("https://example.com")
```

Think:

```text
Launch browser
      ↓
Create isolated session
      ↓
Create tab
      ↓
Open website
```

---

# 28. Closing resources

Always clean up when manually creating resources:

```python
context.close()
browser.close()
```

In a framework, fixtures can handle much of this cleanup automatically.

---

# 29. pytest

A pytest test normally looks like:

```python
def test_homepage():
    assert 1 + 1 == 2
```

The word:

```python
assert
```

is used for verification.

If the condition is true:

```text
PASSED
```

If false:

```text
FAILED
```

---

# 30. Test naming convention

pytest discovers files such as:

```text
test_homepage.py
```

and functions such as:

```python
def test_homepage():
```

A common convention is:

```text
test_*.py
*_test.py
```

and:

```text
test_*
```

for test functions.

---

# 31. Our first Playwright test

Open:

```text
tests/test_homepage.py
```

The important part is:

```python
def test_homepage(page, app_config):
    page.goto(app_config.base_url)
    assert page.title()
```

Here:

```python
page
```

is provided by pytest-playwright.

---

# 32. What is a fixture?

A fixture provides something a test needs.

For example:

```python
def test_homepage(page):
```

`page` is a fixture.

pytest-playwright creates and manages it for us.

Instead of manually writing:

```python
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
```

the plugin can provide:

```python
page
```

directly.

This keeps tests clean.

---

# 33. Important Playwright pytest fixtures

Common fixtures include:

```text
browser
context
page
```

### browser

Provides a browser instance.

### context

Provides a browser context.

### page

Provides a page.

---

# 34. Page fixture example

```python
def test_homepage(page):
    page.goto("https://example.com")
    assert page.title()
```

Flow:

```text
pytest
  ↓
creates Playwright browser/context/page
  ↓
runs test
  ↓
test uses page
  ↓
pytest cleans up
```

---

# 35. Our conftest.py

Open:

```text
tests/conftest.py
```

We have:

```python
import pytest
```

This imports pytest.

Then:

```python
from playwright.config import config
```

This imports our configuration object.

Then:

```python
@pytest.fixture(scope="session")
def app_config():
    return config
```

This creates our own fixture.

---

# 36. What is `@pytest.fixture`?

This:

```python
@pytest.fixture
```

tells pytest:

> The function below is a fixture.

Example:

```python
@pytest.fixture
def username():
    return "admin"
```

Then:

```python
def test_login(username):
    assert username == "admin"
```

pytest automatically supplies the fixture.

---

# 37. What does `scope="session"` mean?

This:

```python
scope="session"
```

means the fixture is created once for the entire pytest session.

Other common scopes are:

```text
function
class
module
package
session
```

For a beginner:

- `function` → once per test
- `session` → once for the whole run

---

# 38. pytest.ini

Open:

```text
pytest.ini
```

We have:

```ini
[pytest]
testpaths = tests
addopts = -v
```

This is pytest configuration.

---

# 39. `testpaths`

```ini
testpaths = tests
```

means:

> Look for tests inside the `tests` folder.

Without this, pytest can search according to its normal discovery rules.

---

# 40. `addopts`

```ini
addopts = -v
```

`-v` means verbose output.

Instead of:

```text
2 passed
```

you get more detailed test information.

---

# 41. pytest markers

We defined:

```ini
markers =
    smoke: smoke tests
    regression: regression tests
```

Then we can write:

```python
@pytest.mark.smoke
def test_homepage():
    ...
```

This labels the test as a smoke test.

---

# 42. Running a marker

Run:

```bash
pytest -m smoke
```

This tells pytest:

> Run tests marked as smoke.

---

# 43. Playwright configuration

Open:

```text
playwright.config.py
```

This file contains project-level Playwright settings.

It uses:

```python
from dotenv import load_dotenv
```

and:

```python
load_dotenv()
```

This loads environment variables from `.env`.

---

# 44. Environment variables

An environment variable is a value provided outside your Python source code.

Example:

```text
BASE_URL=https://example.com
```

Instead of writing:

```python
BASE_URL = "https://example.com"
```

we can use:

```python
os.getenv("BASE_URL")
```

---

# 45. Why use environment variables?

Suppose we have three environments:

```text
DEV
QA
PROD
```

Their URLs might be:

```text
DEV  → https://dev.example.com
QA   → https://qa.example.com
PROD → https://example.com
```

We do not want to change test code every time.

Instead:

```text
Environment
    ↓
.env / CI variables
    ↓
Python config
    ↓
Tests
```

---

# 46. `.env.example`

We have:

```text
.env.example
```

Example:

```text
BASE_URL=https://example.com
PW_TIMEOUT=30000
HEADLESS=true
TEST_USERNAME=your_username
TEST_PASSWORD=your_password
```

This is a template.

It tells developers which variables are required.

---

# 47. `.env`

You can create:

```text
.env
```

based on `.env.example`.

For example:

```text
BASE_URL=https://qa.example.com
PW_TIMEOUT=30000
HEADLESS=true
TEST_USERNAME=qa_user
TEST_PASSWORD=secret
```

Do not commit real credentials.

---

# 48. Why `.env` is in `.gitignore`

Our `.gitignore` contains:

```text
.env
```

This means Git should ignore `.env`.

Why?

Because `.env` may contain:

- passwords
- API keys
- tokens
- private configuration

---

# 49. Secrets management

For local learning:

```text
.env
```

is convenient.

For production CI/CD:

```text
CI/CD Secret Store
```

is preferred.

Examples of secret stores include those provided by CI/CD platforms or cloud secret-management systems.

Never put real secrets directly into source code.

Bad:

```python
PASSWORD = "RealPassword123"
```

Better:

```python
password = os.getenv("TEST_PASSWORD")
```

---

# 50. `os.getenv()`

Example:

```python
import os

username = os.getenv("TEST_USERNAME")
```

Python asks the operating system:

> Do you have a variable named TEST_USERNAME?

If yes, its value is returned.

---

# 51. Default values

Our configuration has:

```python
os.getenv("BASE_URL", "https://example.com")
```

The second argument is a fallback.

Meaning:

> If BASE_URL doesn't exist, use https://example.com.

---

# 52. Type conversion

Environment variables are strings.

For example:

```text
PW_TIMEOUT=30000
```

is read as text.

We convert it:

```python
int(os.getenv("PW_TIMEOUT", "30000"))
```

Now Python gets:

```python
30000
```

as an integer.

---

# 53. Boolean environment variables

We have:

```python
os.getenv("HEADLESS", "true").lower() == "true"
```

If:

```text
HEADLESS=true
```

the expression becomes:

```python
"true" == "true"
```

which is:

```python
True
```

---

# 54. Browser types

Playwright supports:

```text
Chromium
Firefox
WebKit
```

Chromium is the browser engine used by browsers such as Chrome and Edge.

WebKit is the engine associated with Safari.

Firefox uses the Firefox browser engine.

---

# 55. Running Chromium

```bash
pytest --browser chromium
```

---

# 56. Running Firefox

```bash
pytest --browser firefox
```

---

# 57. Running WebKit

```bash
pytest --browser webkit
```

---

# 58. Running multiple browsers

You can specify:

```bash
pytest --browser chromium --browser firefox --browser webkit
```

Conceptually:

```text
Test
 |
 +-- Chromium
 |
 +-- Firefox
 |
 +-- WebKit
```

This is useful for cross-browser testing.

---

# 59. What is browser matrix testing?

A browser matrix means running the same tests across combinations of environments.

For example:

```text
Browser
├── Chromium
├── Firefox
└── WebKit
```

Later you may expand the matrix:

```text
Browser × Environment
```

Example:

```text
Chromium + QA
Firefox   + QA
WebKit    + QA

Chromium + Staging
Firefox   + Staging
WebKit    + Staging
```

In CI/CD this becomes very powerful.

---

# 60. Headless vs headed

Headless means:

> Browser runs without displaying the normal browser window.

Headed means:

> You can see the browser.

Run headed:

```bash
pytest --headed
```

Headed mode is useful when learning and debugging.

Headless mode is common in CI/CD.

---

# 61. Why use headless mode?

Headless execution usually works well for automated environments where no desktop UI is available.

Example:

```text
Developer laptop
    → headed for debugging

CI server
    → headless for automation
```

---

# 62. Running the first test

Activate your virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Install browsers:

```bash
python -m playwright install
```

Then:

```bash
pytest
```

---

# 63. Understanding test execution

When you run:

```bash
pytest
```

the process is roughly:

```text
pytest starts
      ↓
reads pytest.ini
      ↓
finds tests/
      ↓
loads conftest.py
      ↓
loads fixtures
      ↓
starts Playwright browser
      ↓
runs test
      ↓
assertions execute
      ↓
cleanup
      ↓
test result
```

---

# 64. Our homepage test

The test is:

```python
@pytest.mark.smoke
def test_homepage(page, app_config):
    page.goto(app_config.base_url)
    assert page.title()
    assert page.locator("body").is_visible()
```

Let's break it down.

---

# 65. `@pytest.mark.smoke`

```python
@pytest.mark.smoke
```

Labels the test as smoke.

---

# 66. Test function

```python
def test_homepage(page, app_config):
```

This defines the test.

pytest sees the function because its name starts with:

```text
test_
```

---

# 67. `page`

```python
page
```

is the Playwright page fixture.

We can use it immediately.

---

# 68. `app_config`

```python
app_config
```

is our custom fixture.

It gives us configuration.

---

# 69. Navigation

```python
page.goto(app_config.base_url)
```

If:

```text
BASE_URL=https://example.com
```

then Playwright effectively runs:

```python
page.goto("https://example.com")
```

---

# 70. Title assertion

```python
assert page.title()
```

`page.title()` gets the page title.

`assert` checks that the returned value is truthy/non-empty.

A stronger assertion might be:

```python
assert page.title() == "Example Domain"
```

---

# 71. Locator

This:

```python
page.locator("body")
```

creates a locator for the `<body>` element.

Then:

```python
.is_visible()
```

checks whether it is visible.

---

# 72. What is a locator?

A locator identifies an element on a web page.

Examples:

```python
page.get_by_role("button", name="Login")
```

```python
page.get_by_label("Username")
```

```python
page.get_by_text("Welcome")
```

```python
page.locator("#username")
```

Locators are one of the most important Playwright concepts.

---

# 73. Browser vs context vs page fixture test

Open:

```text
tests/test_browser_context_page.py
```

The test demonstrates manual creation:

```python
def test_browser_context_page(browser, app_config):
    context = browser.new_context()
    page = context.new_page()

    page.goto(app_config.base_url)

    assert page.url.startswith(app_config.base_url)

    context.close()
```

Here:

```text
browser
   ↓
context
   ↓
page
```

---

# 74. Why create a context manually?

Sometimes you need custom context configuration.

For example:

```python
context = browser.new_context(
    viewport={"width": 1920, "height": 1080}
)
```

You can configure things such as:

- viewport
- locale
- timezone
- permissions
- storage state
- user agent

---

# 75. What is a Page Object?

Our current `pages/` folder is intentionally empty.

Later we can create:

```text
pages/
├── login_page.py
├── home_page.py
├── dashboard_page.py
└── checkout_page.py
```

A Page Object stores page-specific automation logic.

Example:

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
```

Then the test becomes simpler.

---

# 76. Why Page Objects?

Without Page Objects:

```python
def test_login(page):
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("secret")
    page.get_by_role("button", name="Login").click()
```

With Page Objects:

```python
def test_login(login_page):
    login_page.login("admin", "secret")
```

The test describes the business action.

The page object contains the UI implementation.

---

# 77. What is the `pages` folder?

It will eventually contain:

```text
pages/
```

Page Object classes.

---

# 78. What is the `utils` folder?

It can contain reusable utilities.

Examples:

```text
utils/
├── logger.py
├── date_utils.py
├── file_utils.py
├── api_utils.py
└── data_utils.py
```

The goal is to avoid duplicating the same code across tests.

---

# 79. What is the `data` folder?

It can contain test data.

Examples:

```text
data/
├── users.json
├── products.json
└── test_data.yaml
```

This separates data from test logic.

---

# 80. What is the `reports` folder?

It can contain generated test reports.

Examples:

```text
reports/
├── html/
├── allure/
└── junit/
```

The exact reporting architecture can be added later.

---

# 81. What is the `logs` folder?

It can contain automation logs.

Examples:

```text
logs/
├── test.log
└── error.log
```

Logging becomes extremely important in large frameworks.

---

# 82. What is `.gitignore`?

`.gitignore` tells Git which files/folders should not normally be tracked.

Examples:

```text
.venv/
.env
__pycache__/
.pytest_cache/
test-results/
```

Why ignore them?

Because they are usually:

- generated
- machine-specific
- temporary
- sensitive

---

# 83. What is README.md?

`README.md` is project documentation.

It tells developers:

- what the project is
- how to install it
- how to run tests
- common commands
- troubleshooting information

---

# 84. What is Markdown?

Markdown is a simple text-formatting language.

For example:

```markdown
# Heading

## Subheading

**bold**

`code`
```

It is commonly used for GitHub documentation.

---

# 85. What are shell scripts?

We have:

```text
scripts/install.sh
```

and:

```text
scripts/install.ps1
```

These automate installation.

Linux/macOS:

```bash
./scripts/install.sh
```

PowerShell:

```powershell
.\scripts\install.ps1
```

The exact command may depend on your shell permissions.

---

# 86. Why automate installation?

Imagine onboarding ten developers.

Without a script:

```text
Create venv
Install pip
Install requirements
Install browsers
...
```

With a script:

```text
Run installation script
```

This reduces setup mistakes.

---

# 87. `python -m` explained

You will frequently see:

```bash
python -m pip
```

and:

```bash
python -m playwright
```

`-m` means:

> Execute a Python module as a command.

This can help ensure that the command uses the Python interpreter associated with the environment you selected.

---

# 88. Absolute beginner command sequence

For a new project:

## Step 1

Open terminal.

## Step 2

Go to the project:

```bash
cd playwright_python_framework
```

## Step 3

Create environment:

```bash
python -m venv .venv
```

## Step 4

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

## Step 5

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Step 6

Install browsers:

```bash
python -m playwright install
```

## Step 7

Run tests:

```bash
pytest
```

---

# 89. Run one test

You can run a specific file:

```bash
pytest tests/test_homepage.py
```

---

# 90. Run one test function

You can use:

```bash
pytest tests/test_homepage.py::test_homepage
```

The syntax is:

```text
file.py::function_name
```

---

# 91. Run smoke tests

```bash
pytest -m smoke
```

---

# 92. Run Firefox

```bash
pytest --browser firefox
```

---

# 93. Run WebKit

```bash
pytest --browser webkit
```

---

# 94. Run headed

```bash
pytest --headed
```

You should see the browser.

This is especially useful while learning.

---

# 95. Run with a browser matrix

```bash
pytest --browser chromium --browser firefox --browser webkit
```

This runs the tests against all three browser engines.

---

# 96. Parallel testing

We installed:

```text
pytest-xdist
```

This allows parallel test execution.

Example:

```bash
pytest -n auto
```

`auto` asks the plugin to determine a worker count.

Do not immediately parallelize everything in a beginner project.

First make tests reliable.

Then optimize execution.

---

# 97. A beginner learning order

Do not try to learn the entire framework at once.

Use this order:

```text
1. Python basics
      ↓
2. Virtual environment
      ↓
3. pip
      ↓
4. Playwright installation
      ↓
5. Browser / Context / Page
      ↓
6. Locators
      ↓
7. Actions
      ↓
8. Assertions
      ↓
9. pytest
      ↓
10. Fixtures
      ↓
11. Configuration
      ↓
12. Environment variables
      ↓
13. Page Objects
      ↓
14. Test data
      ↓
15. Reporting
      ↓
16. Parallel execution
      ↓
17. CI/CD
```

---