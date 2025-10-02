# Configuration settings for Simulated Collections API

import os

class Settings:
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    # Add more config variables as needed

settings = Settings()
