import os

from flask import Flask, request
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from ressources.tag import blp as TagBlueprint


stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)