from flask import render_template
from app import app

@app.route('/')
def home():
	return 'this is the homepage'
@app.route('/index')
def index():
	user = {'username': 'Jösh'}
	posts = [
		{
			'author': { 'username': 'One'},
			'body': 'Yeah Whatever'
		},
		{
			'author': { 'username': 'Two'},
			'body': 'Dunno'
		},
		{
			'author': { 'username': 'Three'},
			'body': 'Greatest Hits'
		}

	]
	return render_template('index.html', title='Home', user=user, posts=posts)
