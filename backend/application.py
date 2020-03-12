from flask import Flask
from .config import Config
from pymongo import MongoClient
from flask_cors import CORS
from .custom_encoder import CustomJsonEncoder
app = Flask(__name__)
app.json_encoder = CustomJsonEncoder
app.config.from_object(Config)
CORS(app)

mongo_client = MongoClient(
    host=app.config.get('MONGO_HOST'),
    port=int(app.config.get('MONGO_PORT'))
)

db = mongo_client.testDb
collection = db.products
collection_info = db.trade_info

from backend import routes  # noqa
