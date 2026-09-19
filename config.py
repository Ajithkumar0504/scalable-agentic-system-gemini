import os
from pathlib import Path
from dotenv import load_dotenv

# Always load .env from the same folder as this config.py
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise ValueError(
        f"GEMINI_API_KEY not found.\n"
        f"Expected .env file at: {ENV_FILE}"
    )

print("Gemini configuration loaded successfully.")