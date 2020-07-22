from . import db

class Customer(db.Model):

    __tablename__ = "Customer"
    identification = db.Column(db.String(14), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address=db.Column(db.String(150),  nullable=False)
    phone=db.Column(db.String(30),  nullable=True)
    mail=db.Column(db.String(30), nullable=False)
    
    children = db.relationship("Socket")

    def __init__(self,identification, name, address,phone,mail):
        self.identification = identification
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
    
    def __str__(self):
        return f'identification: {self.identification}, name: {self.name}, address: {self.address}, phone: {self.phone}, mail: {self.mail}'
    
    @staticmethod
    def validator_mail(mail):
        re_email = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(re_email, mail) is not None