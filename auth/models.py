from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    google_id = db.Column(db.String(100), nullable=False)

    @classmethod
    def create(cls, name, email, picture, google_id):
        user = cls(name=name, email=email, picture=picture, google_id=google_id)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def exist(email):
        return User.query.filter_by(email=email).first()

    def __repr__(self):
        return f"User(name={self.name})"
