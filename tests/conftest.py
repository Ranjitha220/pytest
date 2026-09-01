import pytest

from playwright_config import config


@pytest.fixture(scope="session")
def app_config():
    return config
