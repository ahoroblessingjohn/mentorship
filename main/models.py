from datetime import datetime
from . import db



class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(255), nullable=False)
	lname = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')


	def __repr__(self):
		return f"User('{self.fname}', '{self.lname}', '{self.email}', '{self.image_file}'"