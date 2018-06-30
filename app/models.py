from app import db

class CarPart(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    body = db.Column(db.String(140))

    def __repr__(self):
        return f"<CAR PART: {self.name}>"

    def avatar(self):
        pass
