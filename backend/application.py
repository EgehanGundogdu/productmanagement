from flask import Flask
from .config import Config
from pymongo import MongoClient

app = Flask(__name__)

app.config.from_object(Config)

mongo_client = MongoClient(
    host=app.config.get('MONGO_HOST'),
    port=int(app.config.get('MONGO_PORT'))
)

db = mongo_client.testDb
collection = db.productManagement
from backend import routes  # noqa
