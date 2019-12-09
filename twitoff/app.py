from decouple import config
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

	@app.route('/iris')
	def iris():    
		from sklearn.datasets import load_iris
		from sklearn.linear_model import LogisticRegression
		X, y = load_iris(return_X_y=True)
		clf = LogisticRegression(
			random_state=0, 
			solver='lbfgs', 
			multi_class='multinomial').fit(X, y)
		return str(clf.predict(X[:2, :]))

	return app