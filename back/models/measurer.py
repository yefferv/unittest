from . import db

class Measurer(db.Model):

    __tablename__ = "Measurer"
    id =db.Column(db.Integer, primary_key=True)
    reference =db.Column(db.String(30), nullable=False)
    nominal_voltage=db.Column(db.String(30),  nullable=False)
    nominal_current=db.Column(db.String(30),  nullable=False)
    active_energy=db.Column(db.String(30),  nullable=False)
    reactive_energy=db.Column(db.String(30),  nullable=False)
    storage_capacity=db.Column(db.String(30),  nullable=False)

    socket_code = db.Column(db.String(30), db.ForeignKey('Socket.code'), nullable=False)
    
    def __init__(self,reference,nominal_voltage,nominal_current,active_energy,reactive_energy,storage_capacity,socket_code):
        self.reference = reference
        self.nominal_voltage = nominal_voltage
        self.nominal_current = nominal_current
        self.active_energy = active_energy
        self.reactive_energy = reactive_energy  
        self.storage_capacity = storage_capacity
        self.socket_code = socket_code