from dotenv import load_dotenv, find_dotenv
from pathlib import Path  # python3 only
import os

# set path to env file
env_path = Path('.') / '.env'
load_dotenv(find_dotenv())
# load_dotenv(dotenv_path=env_path)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY1')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL1')
