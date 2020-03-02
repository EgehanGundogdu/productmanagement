from dotenv import load_dotenv
from os.path import join, dirname
import os

env_file = load_dotenv(join(dirname(__file__), '.env'))


class Config:
    MONGO_HOST = os.environ.get('MONGO_HOST')
    MONGO_PORT = os.environ.get('MONGO_PORT')
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret key will be change"
