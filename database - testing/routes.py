from flask import Flask,render_template
from base64 import b64encode
from models import db, image1

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@127.0.0.1/image'

db.init_app(app)

@app.route('/')
def hello_world():
	images = image1.query.all()

	for image in images:
		print "gg"
		image.image = b64encode(image.image)
		print image.image
	print images

	return render_template('home.html',images=images)

if __name__ == '__main__':
   app.run(debug=True)

