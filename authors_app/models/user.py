from authors_app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=True)
    books = db.relationship('Book', backref='user')
    user_type = db.Column(db.String(20), default='author')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, first_name, last_name, email, contact, password, biography, user_type, image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_type = user_type
        self.contact = contact
        self.image = image
        self.biography = biography
        self.password = password