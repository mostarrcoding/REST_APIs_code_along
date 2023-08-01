from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        raise NotImplementedError("Getting an item is not implemented.")
        #NotImplementedError(error_string): derived from RuntimeError
        #which itself is raised "when an error is detected that doesn’t
        #fall in any of the other categories" (Python docs 3.11.4)

    def delete(self, item_id):
        raise NotImplementedError("Deleting an item is not implemented.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        raise NotImplementedError("Updating an item is not implemented.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        raise NotImplementedError("Listing items is not implemented.")

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        raise NotImplementedError("Creating an item is not implemented.")
