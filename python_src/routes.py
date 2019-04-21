from python_src import app
from python_src.models import Student, Building
from python_src import db_connection as db_conn
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required,\
    logout_user, current_user
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Email, Length


app.config['SECRET_KEY'] = 'asdf'
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_email):
    return Student.get(user_email)


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(max=50)])
    password = StringField('password', validators=[InputRequired(), Length(max=25)])
    remember = BooleanField('remember me')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if db_conn.are_valid_credentials(form.email.data, form.password.data):
            login_user(Student.get(form.email.data), remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            return '<h1> Invalid credentials </h1>'
    return render_template("index.html", form=form)


@app.route('/')
@app.route('/home', methods=['GET'])
@login_required
def home():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("home.html", all_building_names=all_building_names)


@app.route('/new_route', methods=['GET'])
@login_required
def new_route():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("new_route.html", all_building_names=all_building_names)


@app.route('/edit_schedule', methods=['GET'])
@login_required
def edit_schedule():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("edit_schedule.html", all_building_names=all_building_names)


@app.route('/settings')
@login_required
def settings():
    return render_template("settings.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

