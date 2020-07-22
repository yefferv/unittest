from flask import request,  jsonify
from flask import current_app as app
from back.models.socket import Socket
from back.models import db
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)
class SocketSchema(ma.Schema):
    class Meta:
        fields = ('code','city', 'address', 'coordinateX','coordinateY','customer_identification')


socket_schema = SocketSchema()
sockets_schema = SocketSchema(many=True)


@app.route('/sockets', methods=['GET'])
def get_sockets():
    all_sockets = Socket.query.all()
    result = sockets_schema.dump(all_sockets)
    return jsonify(result)

@app.route('/sockets/<id>', methods=['GET'])
def get_socket(id):
  socket = Socket.query.get(id)
  return socket_schema.jsonify(socket)


@app.route('/sockets', methods=['POST'])
def create_socket():
    code = request.json['code']
    city = request.json['city']
    address = request.json['address']
    coordinateX = request.json['coordinateX']
    coordinateY = request.json['coordinateY']
    customer_identification = request.json['customer_identification']


    new_socket= Socket(code,city,address,coordinateX,coordinateY,customer_identification)
    db.session.add(new_socket)
    db.session.commit() 
    return socket_schema.jsonify(new_socket)


@app.route('/sockets/<id>', methods=['PUT'])
def update_socket(id):
    socket = Socket.query.get(id)

    #socket.code = request.json['code']
    socket.city = request.json['city']
    socket.address = request.json['address']
    socket.coordinateX = request.json['coordinateX']
    socket.coordinateY = request.json['coordinateY']
    socket.customer_identification = request.json['customer_identification']

    db.session.commit()
    return socket_schema.jsonify(socket)

@app.route('/sockets/<id>', methods=['DELETE'])
def delete_socket(id):
  socket = Socket.query.get(id)
  db.session.delete(socket)
  db.session.commit()
  return socket_schema.jsonify(socket)

