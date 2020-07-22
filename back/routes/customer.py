from flask import request,  jsonify
from flask import current_app as app
from back.models.customer import Customer
from back.models import db
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from back.utils.validators import validator_mail

ma = Marshmallow(app)
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('identification','name', 'address', 'phone','mail')


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


@app.route('/customers', methods=['GET'])
def get_customers():
    all_customers = Customer.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result)

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
  customer = Customer.query.get(id)
  return customer_schema.jsonify(customer)


@app.route('/customers', methods=['POST'])
def create_customer():
    identification = request.json['identification']
    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    mail = request.json['mail']

    flag = validator_mail(mail)
    if flag:
        new_customer = Customer(identification,name,address,phone,mail)
        db.session.add(new_customer)
        db.session.commit()
    else:
        new_customer = Customer(identification,name,address,phone,mail)

    return customer_schema.jsonify(new_customer)    


@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)

    customer.name = request.json['name']
    customer.address = request.json['address']
    customer.phone = request.json['phone']
    customer.mail = request.json['mail']

    db.session.commit()
    return customer_schema.jsonify(customer)

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get(id)
        if (customer != None):
            db.session.delete(customer)
            db.session.commit()
    except Exception as e:
        print('error delete')
        print(e)
    return jsonify({'message': 'Register remove'})


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API REST'})
