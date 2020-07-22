from flask import request,  jsonify
from flask import current_app as app
from back.models.measurer import Measurer
from back.models import db
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)
class MeasurerSchema(ma.Schema):
    class Meta:
        fields = ('reference','nominal_voltage', 'nominal_current', 'active_energy','reactive_energy','storage_capacity','socket_code')


measurer_schema = MeasurerSchema()
measurers_schema = MeasurerSchema(many=True)


@app.route('/measurers', methods=['GET'])
def get_measurers():
    all_measurers = Measurer.query.all()
    result = measurers_schema.dump(all_measurers)
    return jsonify(result)

@app.route('/measurers/<id>', methods=['GET'])
def get_measurer(id):
  measurer = Measurer.query.get(id)
  return measurer_schema.jsonify(measurer)


@app.route('/measurers', methods=['POST'])
def create_measurer():

    reference = request.json['reference']
    nominal_voltage = request.json['nominal_voltage']
    nominal_current = request.json['nominal_current']
    active_energy = request.json['active_energy']
    reactive_energy = request.json['reactive_energy']
    storage_capacity = request.json['storage_capacity']
    socket_code = request.json['socket_code']

    new_measurer= Measurer(reference,nominal_voltage,nominal_current,active_energy,reactive_energy,storage_capacity,socket_code)
    db.session.add(new_measurer)
    db.session.commit() 
    return measurer_schema.jsonify(new_measurer)


@app.route('/measurers/<id>', methods=['PUT'])
def update_measurer(id):
    measurer = Measurer.query.get(id)

    measurer.reference = request.json['reference']
    measurer.nominal_voltage = request.json['nominal_voltage']
    measurer.nominal_current = request.json['nominal_current']
    measurer.active_energy = request.json['active_energy']
    measurer.reactive_energy = request.json['reactive_energy']
    measurer.storage_capacity = request.json['storage_capacity']
    measurer.socket_code = request.json['socket_code']

    db.session.commit()
    return measurer_schema.jsonify(measurer)

@app.route('/measurers/<id>', methods=['DELETE'])
def delete_measurer(id):
  measurer = Measurer.query.get(id)
  db.session.delete(measurer)
  db.session.commit()
  return measurer_schema.jsonify(measurer)

