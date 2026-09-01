from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class PlaywrightConfig:
    base_url: str = os.getenv("BASE_URL", "https://example.com")
    timeout: int = int(os.getenv("PW_TIMEOUT", "30000"))
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"


config = PlaywrightConfig()
