from decouple import config
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
	app.config['ENV'] = config('ENV')
	DB.init_app(app)

	@app.route('/')
	def root():
		# users = User.query.all()
		return render_template('base.html', title='hello')

	@app.route('/reset')
	def reset():
		DB.drop_all()
		DB.create_all()
		return render_template('base.html', title='hello')

	return app