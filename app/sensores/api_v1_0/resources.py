from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import HumedadSchema, TemperaturaSchema
from ..models import Humedad, Temperatura, Usuario

sensores_v1_0_bp = Blueprint('sensores_v1_0_bp', __name__)

humedad_schema = HumedadSchema()
temperatura_schema = TemperaturaSchema()

api = Api(sensores_v1_0_bp)

class HumedadListResource(Resource):
    def get(self):
        humedades = Humedad.get_all()
        result = humedad_schema.dump(humedades, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        humedad_dict = humedad_schema.load(data)
        humedad = Humedad(valor=humedad_dict['valor'], timestamp=humedad_dict['timestamp'], status=humedad_dict['status'], usuario_id=humedad_dict['usuario_id'])
        humedad.save()
        resp = humedad_schema.dump(humedad)
        return resp, 201

class HumedadResource(Resource):
    def get(self, humedad_id):
        humedad = Humedad.get_by_id(humedad_id)
        if humedad is None:
            raise ObjectNotFound('La película no existe')
        resp = humedad_schema.dump(humedad)
        return resp
    
    def put(self, humedad_id):
        humedad = Humedad.get_by_id(humedad_id)
        data = request.get_json()
        humedad_dict = humedad_schema.load(data)
        humedad.valor = humedad_dict["valor"]
        humedad.timestamp = humedad_dict["timestamp"]
        humedad.status = humedad_dict["status"]
        humedad.usuario_id = humedad_dict["usuario_id"]
        humedad.save()
        resp = humedad_schema.dump(humedad)
        return resp, 200

    #def delete(self, humedad_id):
    #    humedad = Humedad.get_by_id(humedad_id)
    #    humedad.delete()
    #    return "", 204
    
    # Borrado Lógico
    def delete(self, humedad_id):
        humedad = Humedad.get_by_id(humedad_id)
        humedad.status = 'I'
        humedad.save()
        resp = humedad_schema.dump(humedad)
        return resp, 200

class TemperaturaListResource(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

class TemperaturaResource(Resource):
    def get(self, temperatura_id):
        pass
    
    def put(self, temperatura_id):
        pass

    def delete(self, temperatura_id):
        pass

api.add_resource(HumedadListResource, '/api/v1.0/humedad/', endpoint='humedad_list_resource')
api.add_resource(HumedadResource, '/api/v1.0/humedad/<int:humedad_id>', endpoint='humedad_resource')
api.add_resource(TemperaturaListResource, '/api/v1.0/temperatura/', endpoint='temperatura_list_resource')
api.add_resource(TemperaturaResource, '/api/v1.0/temperatura/<int:temperatura_id>', endpoint='temperatura_resource')
