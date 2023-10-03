from marshmallow import fields

from app.ext import ma

class HumedadSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    valor = fields.Number()
    timestamp = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class TemperaturaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    valor = fields.Number()
    timestamp = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class LuminosidadSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    valor = fields.Number()
    timestamp = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class MovimientoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    timestamp = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class DistanciaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    valor = fields.Number()
    timestamp = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class UsuarioSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    usuario = fields.String()
    password = fields.String()
    token = fields.String()
