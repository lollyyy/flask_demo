from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm

@app.route('/')
def home():
	return render_template('base.html', title='Home')
	
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
	return render_template('index.html', title='Index', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
