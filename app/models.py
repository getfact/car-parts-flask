from datetime import datetime
from app import db

class CarPart(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image_url = db.Column(db.String(124))

    def __repr__(self):
        return f"<CAR PART: {self.name}>"

    def image(self, size):
        digest = md5(self.name.lower().encode('utf-8')).hexdigest()
        return self.image_url.format(digest, size)

def load_part(id):
    return CarPart(int(id))
