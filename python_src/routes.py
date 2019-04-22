from python_src import app
from python_src.models import Student, Building
from python_src.path_finding import find_optimal_class_path, path_to_gmaps_link
from flask import render_template, flash, redirect, url_for
from python_src.forms import PasswordChange,DeleteAccount, ResetAccount
from python_src.models import Student
from python_src import db_connection as db_conn
from python_src.path_finding import get_best_path, path_to_gmaps_link, display_path
from python_src.db_connection import get_graph
from python_src.forms import PasswordChange
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required,\
    logout_user, current_user
from wtforms import StringField, BooleanField, TimeField
from wtforms.validators import InputRequired, Email, Length
from wtforms_components import TimeField
from flask import Flask, request

<<<<<<< HEAD
# app = Flask(__name__)
=======

>>>>>>> 8e15d1013bb2f64a923a78a7e59e37a24c74348a
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


class TimeForm(FlaskForm):
    start_time = TimeField('time', validators=[InputRequired()])
    end_time = TimeField('time', validators=[InputRequired()])


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
    current_weekly_schedule = current_user.todays_schedule()
    paths = find_optimal_class_path(None, current_weekly_schedule)
    paths.insert(0, [])
    print(paths)
    links = [[] if i == 0 else path_to_gmaps_link(p) for i, p in enumerate(paths)]
    print(paths)
    print(len(paths))
    print(current_weekly_schedule)
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("home.html", current_weekly_schedule=zip(current_weekly_schedule, links),
                           all_building_names=all_building_names)

@app.route('/home')
def about():
    return render_template("home.html")


@app.route('/new_route', methods=['GET', 'POST'])
@login_required
def new_route():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    if request.method == "GET":
        return render_template("new_route.html", all_building_names=all_building_names)
    else:
        start_loc = request.form.get('start_loc')
        end_loc = request.form.get('end_loc')
        print("Start Location:", start_loc)
        print("End Location:", end_loc)
        start = None
        end   = None
        for currentNode in get_graph().keys():
            if currentNode.building == start_loc:
                start = currentNode
                # print("Start: ", start)
            if currentNode.building == end_loc:
                end = currentNode
                #print("End: ", end)

        bestpath = get_best_path(get_graph(), start, end)
        if bestpath is not None:
            display_path(path_to_gmaps_link(bestpath))
        return render_template("new_route.html", gmaps_link=path_to_gmaps_link(bestpath), all_building_names=all_building_names, start_loc=start_loc, end_loc=end_loc)

@app.route('/edit_schedule', methods=['GET'])
@login_required
def edit_schedule():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    tf = TimeForm()
    return render_template("edit_schedule.html", form=tf, all_building_names=all_building_names)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = PasswordChange()
    delete_account_form = DeleteAccount()
    reset_account_form = ResetAccount()

    if form.submit.data and form.validate_on_submit():
        current_user.update_password(form.new_password.data)
        flash('Password Changed', 'success')
    if delete_account_form.delete_account_confirmation.data == 'delete':
        current_user.delete_account()
        print("DELETING ACCOUNT")
    if reset_account_form.reset_account_confirmation.data == 'reset':
        current_user.reset_account()
        print("Reset ACCOUNT")
    return render_template("settings.html",  form=form, title="password_change", delete_account_form=delete_account_form, reset_account_form=reset_account_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

