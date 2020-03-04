from flask import Flask
from .config import Config
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)

app.config.from_object(Config)
CORS(app)

mongo_client = MongoClient(
    host=app.config.get('MONGO_HOST'),
    port=int(app.config.get('MONGO_PORT'))
)

db = mongo_client.testDb
collection = db.productManagement
from backend import routes  # noqa
