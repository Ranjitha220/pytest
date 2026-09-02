from dataclasses import dataclass
import os

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class PlaywrightConfig:
    base_url: str = os.getenv("BASE_URL", "https://www.akbartravels.com/in")
    timeout: int = int(os.getenv("PW_TIMEOUT", "30000"))
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"


config = PlaywrightConfig()
