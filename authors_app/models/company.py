from authors_app import db
from datetime import datetime




class company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique=True)
    origin = db.Column(db.String(100))
    description =db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("user", backref="companies")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)


    def __init__(self, name, description, origin):
        self.name=name
        self.description=description
        self.origin=origin

        


    def __init__(self):
        return f"<Company(name='{self.name}', origin='{self.origin})>"