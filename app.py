from flask import Flask, render_template, url_for, request, flash, redirect
from model import db, Users
from config.config import DATABASE_URI, SECRET_KEY
from flask_login import LoginManager, current_user, login_user, logout_user

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.secret_key = SECRET_KEY
db.init_app(app)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def show():
    if current_user.is_authenticated:
        flash('Login successfully')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('show'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            user = Users.query.filter_by(username=username).first()
            if user is None or password != user.password:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('show'))
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out!')
        return redirect(url_for('show'))
    else:
        flash("You aren't login")
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
