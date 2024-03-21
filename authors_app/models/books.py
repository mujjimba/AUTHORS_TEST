from authors_app import db
from datetime import datetime


class Book(db.Model):
    __tablename__='books'
    id=db.Column(db.Integer,primary_key=True)#all datatypes start with capital letter eg Integer,String
    title=db.Column(db.String(50),nullable=False)
    price=db.Column(db.String(100),nullable=False)
    pages=db.Column(db.Integer)
    description=db.Column(db.String(100))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    company_id=db.Column(db.Integer,db.ForeignKey('companies.id'))
    publication_date=db.Column(db.Date,nullable=False)
    isbn = db.Column(db.String(30), nullable=True, unique=True)
    genre = db.Column(db.String(50), nullable=False)

    #user=db.relationship('user',backref='books')
    #company=db.relationship('company',backref='books')
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())
    def __init__(self,title,description,pages,image,price,price_unit,publication_date,isbn,genre,user_id,):
        self.title=title
        self.description=description
        self.price = price
        self.price_unit = price_unit
        self.pages = pages
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.user_id = user_id
        self.image = image

        self.user_id=user_id
        self.pages=pages
    def __init__(self):
        return f'<Book{self.title}'


