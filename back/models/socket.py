from . import db

class Socket(db.Model):

    __tablename__ = "Socket"
    code =db.Column(db.String(30), primary_key=True)
    city=db.Column(db.String(50),  nullable=False)
    address=db.Column(db.String(150),  nullable=False)
    coordinateX=db.Column(db.String(20),  nullable=False)
    coordinateY=db.Column(db.String(20),  nullable=False)


    customer_identification = db.Column(db.String(14), db.ForeignKey('Customer.identification'), nullable=False)
    
    children = db.relationship("Measurer")
    
    def __init__(self,code,city,address,coordinateX,coordinateY,customer_identification):
        self.code = code
        self.city = city
        self.address = address
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY  
        self.customer_identification = customer_identification