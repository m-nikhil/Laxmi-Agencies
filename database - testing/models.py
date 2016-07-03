from flask.ext.sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class image1(db.Model):
	__tablename__ = 'image1'
	name = db.Column(db.String(30),primary_key=True)
	image = db.Column(db.LargeBinary)
