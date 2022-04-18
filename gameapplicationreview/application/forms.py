from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import Length, DataRequired

class UserForm(FlaskForm):
    first_name = StringField("Enter your first name")
    last_name = StringField("Enter your last name")
    user_email = StringField("Please enter your email address")
    user_number = StringField("Please enter your contact number")
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm):
    videogame = StringField("Enter the videogame")
    review_rating = StringField("Please provide a rating of 0-10 of the videogame")
    review_description = StringField("What did you think of the game, please go into details (character limit 500)")
    review_date = DateField("Date of review")
    submit = SubmitField("Submit your review")