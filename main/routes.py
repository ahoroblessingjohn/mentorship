from re import A
from flask import render_template, request, url_for, redirect, session
from . import app, db
from .models import User
import bcrypt

def Authenticated():
    if 'user_id' in session:
        return True
    return False

def getUser():
    id = session["user_id"]
    user = User.query.filter_by(id=int(id)).first()
    return user


@app.route('/')
def home():
    context = {
        'title': "Home"
    }
    return render_template('home.html', context=context)


@app.route('/courses')
def courses():
    context = {
        'title': 'Courses'
    }
    return render_template('courses.html', context=context)

@app.route('/about')
def about():
    context = {
        'title': 'About'
    }
    return render_template('about.html', context=context)

@app.route('/contact')
def contact():
    context = {
        'title': 'Contact'
    }
    return render_template('contact.html', context=context)


@app.route('/login',  methods=['POST', 'GET'])
def login():
    context = {
        'title': 'Login'
    }
    if Authenticated():
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        user = User.query.filter_by(email='jonathanfelicity@mail.com').first()
        if user:
            salt = bcrypt.gensalt()
            password =  bytes(request.form.get("password"), 'utf-8')
            if bcrypt.checkpw(password, user.password):
                session['user_id'] = user.id
                return redirect(url_for('dashboard'))
            else:
                return "Wrong password"
        return "NO user"
    return render_template('auth/login.html', context=context)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    context = {
        'title': 'Sign Up'
    }
    if Authenticated():
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes(request.form.get("password"), 'utf-8'), salt)
        user = User(fname=request.form.get("fname"), lname=request.form.get("lname"), email=request.form.get("email"), password=hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('auth/signup.html', context=context)



@app.route('/dashboard')
def dashboard():
    if Authenticated():
        user = getUser()
        return render_template('accounts/dashboard.html', user=user)
        
    return redirect(url_for('login'))


@app.route('/settings')
def settings():
    if Authenticated():
        user = getUser()
        return render_template('accounts/settings.html', user=user)
        
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404