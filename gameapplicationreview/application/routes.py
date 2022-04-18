#Installing all modules required for my routes.py
from application import app, db
from application.forms import UserForm
from application.forms import ReviewForm
from application.models import User, Review
from flask import render_template, request, redirect, url_for

#Route for index page.
@app.route('/')
def index():
    #Presents all of the users that have left a review on the database.
    all_users = User.query.all()
    #Returns the index page with all users presented.
    return render_template('/index.html', all_users = all_users)

#Route for user_reviews page.
@app.route('/user_reviews/<int:account_id>')
def user_reviews(account_id):
    #Queries the database for all user reviews left by a specific user according to their unique account ID.
    all_reviews = Review.query.filter_by(account_id = account_id).all()
    #Provides the 'user_reviews' page. Each user has a button underneath their information, when clicked it will take you to this page which presents all the reviews a user has left.
    return render_template('/user_reviews.html', all_reviews = all_reviews)

#Route for new_user page.
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    #Defining the form to use.
    form = UserForm()
    #If the request method is 'POST', then you will get a page to input all user information including: First name, Last name, Email address, Contact number.
    if request.method == "POST":
        user = User(first_name = form.first_name.data, last_name = form.last_name.data, user_email = form.user_email.data, user_number = form.user_number.data)
        #Sending the information put into the fields to the database.
        db.session.add(user)
        db.session.commit()
        #After information has been submitted, the user will be redirected back to the index page with all of their information presented.
        #They are then able to add a review or view the reviews added by the user/other users.
        return redirect(url_for('index'))
    
    return render_template('new_user.html', form = form)

#Route for new_rating page.
@app.route('/new_rating/<int:account_id>', methods=['GET', 'POST'])
def new_rating(account_id):
    #Defining the form which needs to be used.
    form = ReviewForm()

    #If the request method is 'POST' then the form to input a new review is presented which consists of: Videogame, Review rating, Review description, Date of review
    if request.method == "POST":
        review = Review(account_id = account_id, videogame = form.videogame.data, review_rating = form.review_rating.data, review_description = form.review_description.data, review_date = form.review_date.data)
        #Sending the information put into the fields to the database.
        db.session.add(review)
        db.session.commit()
        #After the information has been submitted, the 'user_reviews' page will be presented, on which you can see each review which has been left by a specific user.
        return redirect(url_for('user_reviews', account_id = account_id))
    
    return render_template('new_rating.html', form = form)

#Route for delete_review page.
#The '<int:id>' is referencing the unique ID of the user. Keep in mind, this is not the same as the unique ID of a review, this ID is not visible by users and only visible in the database.
@app.route('/delete_review/<int:id>')
def delete_review(id):
    #Querying the database to retreive all the reviews which have been left by a user. 
    review = Review.query.get(id)
    #Deletes the review put into the database previously.
    db.session.delete(review)
    db.session.commit()
    #After the review has been deleted, the user will be redirected to the index page.
    return redirect(url_for('index'))

#Route for update_review page.
@app.route('/update_review/<int:id>', methods = ['GET', 'POST'])
def update_review(id):
    #Retrieves all the reviews left by a user.
    review = Review.query.get(id)
    #Defining the form to use.
    form = ReviewForm()

    #If a user wants to update an existing review, the request method would be 'POST' and the user will be presented with the same 'ReviewForm' with the previous information they put in.
    #From here, the user can edit the fields they inputted.
    if request.method == "POST":
        review.videogame = form.videogame.data
        review.review_rating = form.review_rating.data
        review.review_description = form.review_description.data
        review.review_date = form.review_date.data
        db.session.commit()
        #After the user has update the review, they are redirected to the index page.
        return redirect(url_for('index'))
    #References the form to use.
    form.videogame.data = review.videogame
    form.review_rating.data = review.review_rating
    form.review_description.data = review.review_description
    form.review_date.data = review.review_date

    return render_template('new_rating.html', form = form)

