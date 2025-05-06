import os
from dotenv import load_dotenv
from pathlib import Path

# Load the .env file
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    # Read variables from .env
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    APP_TYPE = os.getenv('APP_TYPE', 'local')
    DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1')

config = Config()