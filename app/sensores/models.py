#from operator import length_hint
#from sqlalchemy.orm import backref
from app.db import db, BaseModelMixin

class Humedad(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Numeric)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, valor, timestamp, status, usuario_id):
        self.valor = valor
        self.timestamp = timestamp
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Humedad({self.valor})'
    def __str__(self):
        return f'{self.valor}'

class Temperatura(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, valor, timestamp, status, usuario_id):
        self.valor = valor
        self.timestamp = timestamp
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Temperatura({self.valor})'
    def __str__(self):
        return f'{self.valor}'

class Luminosidad(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, valor, timestamp, status, usuario_id):
        self.valor = valor
        self.timestamp = timestamp
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Luminosidad({self.valor})'
    def __str__(self):
        return f'{self.valor}'

class Movimiento(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, valor, timestamp, status, usuario_id):
        self.valor = valor
        self.timestamp = timestamp
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Movimiento({self.valor})'
    def __str__(self):
        return f'{self.valor}'

class Distancia(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, valor, timestamp, status, usuario_id):
        self.valor = valor
        self.timestamp = timestamp
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Distancia({self.valor})'
    def __str__(self):
        return f'{self.valor}'

class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    password = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.token = ""

    def __repr__(self):
        return f'Usuario({self.usuario})'
    def __str__(self):
        return f'{self.usuario}'
