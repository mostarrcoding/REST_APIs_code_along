from marshmallow import Schema, fields
#marshmallow not to be confused w/the Django imaging module Pillow
#Schemas are from marshmallow


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


#marshmallow creates schemas for serializing and
#deserializing data
#
#"...mapping attribute names to Field objects."
#                           -marshmallow quick start
#
#deserializing objects ~= "loading"
#serializing objects ~= "dumping"
#https://marshmallow.readthedocs.io/en/stable/quickstart.html