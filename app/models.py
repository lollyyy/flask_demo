from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as hashgen
from werkzeug.security import check_password_hash as hashcheck


class User(UserMixin, db.Model):
	# Declare User properties
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	# Declare methods for User
	def __repr__(self):
		return '<User {}>'.format(self.username)

	# Methods for hashing and checking password
	def set_password(self, password):
		self.password_hash = hashgen(password)

	def check_password(self, password):
		return hashcheck(self.password_hash, password)

class Post(db.Model):
	# Declare Post props
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	# Declare Post methods
	def __repr__(self):
		return '<Post {}>'.format(self.body)

# User loader function for flask-login
@login.user_loader
def load_user(id):
	return User.query.get(int(id))