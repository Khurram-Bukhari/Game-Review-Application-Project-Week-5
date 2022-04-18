from application import app, db
from datetime import datetime

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(70),nullable = False)
    last_name = db.Column(db.String(70), nullable = False)
    user_email = db.Column(db.String(100), nullable = False)
    user_number = db.Column(db.Integer, nullable = False, default = '0000000000')
    reviews = db.relationship("Review", backref = "reviewbr")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    videogame = db.Column(db.String(50), nullable = False)
    review_rating = db.Column(db.String(2), nullable = False)
    review_description = db.Column(db.String(500), nullable = False)
    review_date = db.Column(db.DateTime, nullable = False, default = datetime.now)
    account_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable = False)


