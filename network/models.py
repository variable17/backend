import enum
from extensions import db


class ProviderTypeEnum(enum.Enum):
    Hospital = 'Hospital'
    Pharmacy = 'Pharmacy'
    Clinic = 'Clinic'


class NetworkProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    pin_code = db.Column(db.Integer, nullable=False, index=True)
    website = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Enum(ProviderTypeEnum), nullable=False)

    def __repr__(self):
        return self.name

    @staticmethod
    def find_by_pin_code(pin_code):
        return NetworkProvider.query.filter_by(pin_code=pin_code)



