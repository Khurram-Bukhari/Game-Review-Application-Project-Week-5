from flask_testing import TestCase
from flask import url_for
from application import app, db
from application.models import User, Review
from flask_sqlalchemy import SQLAlchemy
import pytest

from flask_testing import TestCase
from flask import url_for
from application import app, db
from application.models import User, Review
from flask_sqlalchemy import SQLAlchemy
import pytest

class TestBase (TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:thisismyproject@10.36.1.4/gamep1",
            WTF_CSRF_ENABLED = False
        )
        return app


    def setUp(self):
        db.create_all()
        user_1 = User(first_name = 'Syed', last_name = 'Bukhari', user_email = 'Khurram-bukhari@hotmail.com')
        review_1 = Review(account_id = 1, videogame = 'Call of Duty', review_rating = '7', review_description = 'This game was amazing.')
        db.session.add(user_1)
        db.session.add(review_1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestAddReview(TestBase):
    def test_view_review(self):
        response = self.client.get(url_for('new_rating', account_id = 1))
        self.assertEqual(response.status_code, 200)

     
    def test_view_user(self):
        response = self.client.get(url_for('new_user'))
        self.assertEqual(response.status_code, 200)

    
    def test_user_form(self):
        response = self.client.post(
            url_for('new_user'), 
            data = dict(
                first_name = "Syed",
                last_name = 'Bukhari',
                user_email = 'Khurram-bukhari@hotmail.com'
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_review_form(self):
        response = self.client.post(
            url_for('new_rating', account_id = 1), 
            data = dict(
                videogame = 'Call of Duty Warzone',
                review_rating = '10',
                review_description = 'Fantastic game'
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    
    def test_review_delete(self):
        response = self.client.get(url_for('delete_review', id = 1))
        self.assertNotIn(b'videogame', response.data)
    
class TestUpdate(TestBase):
    def test_review_update(self):
        response = self.client.post(
            url_for('update_review', id = 1),
            data = dict(
                review = "Call of Duty"
            ),
            follow_redirects = True
        )
        self.assertIn(b"", response.data)
            