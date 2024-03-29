from datetime import datetime
from python_src import app
from python_src.models import Building, Student
from flask import render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user
from python_src.forms import PasswordChange, DeleteAccount, ResetAccount, RegistrationForm
from python_src.path_finding import get_best_path, path_to_gmaps_link, display_path, find_optimal_class_path
from python_src import db_connection as db_conn
from python_src.forms import PasswordChange
from wtforms import StringField, BooleanField, TimeField
from wtforms.validators import InputRequired, Email, Length
from wtforms_components import TimeField
from wtforms.widgets import PasswordInput
from python_src.models import get_graph, get_weekly_schedule_study, StudyInfo


# app = Flask(__name__)

Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_email):
    return Student.get(user_email)


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(max=50)])
    password = StringField('password', validators=[InputRequired(), Length(max=25)],
                           widget=PasswordInput(hide_value=True))
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
    return render_template('index.html', form=form)


@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    form = RegistrationForm()
    if form.validate_on_submit():
        stud = Student(email=form.email.data,
                       first_name=form.first_name.data,
                       last_name=form.last_name.data,
                       password=form.password.data)
        db_conn.create_student(stud, )
        return redirect(url_for('login'))
    return render_template('create_account.html', form=form)

@app.route('/')
@app.route('/home', methods=['GET'])
@login_required
def home():
    if datetime.today().weekday() < 5:
        todays_schedule = get_weekly_schedule_study(current_user)[datetime.today().weekday()]
    else:
        todays_schedule = []
    todays_schedule.sort(key=lambda _: _.start_time)
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    return render_template('home.html', datetime=datetime, current_weekly_schedule=todays_schedule,
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
        end = None
        for currentNode in get_graph().keys():
            if currentNode.building == start_loc:
                start = currentNode
                # print("Start: ", start)
            if currentNode.building == end_loc:
                end = currentNode
                #print("End: ", end)

        bestpath = get_best_path(get_graph(), start, end)
        if bestpath is not None:
            display_path(path_to_gmaps_link(bestpath[0]))
        return render_template("new_route.html", gmaps_link=path_to_gmaps_link(bestpath[0]),
                               all_building_names=all_building_names, start_loc=start_loc, end_loc=end_loc)


@app.route('/edit_schedule', methods=['GET', 'POST'])
@login_required
def edit_schedule():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    tf = TimeForm()

    if request.method == 'POST':
        del_class_name = request.form.get('del_class_name')
        if del_class_name is not None and del_class_name != '-1':
            year, semester, class_name = del_class_name.split(' ')
            current_user.delete_class(year, semester, class_name)

        year = request.form.get('year')
        semester = request.form.get('semester')
        building = request.form.get('building')
        week_days = [request.form.get(_) for _ in 'MTWRF'
                     if request.form.get(_) is not None]
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        class_name = request.form.get('class_name')

        is_invalid = False
        for _ in [year, semester, building, start_time, end_time]:
            # check to make sure each input is filled in
            if _ is None or _ == '-1':
                is_invalid = True
                break
        if len(week_days) < 1:
            is_invalid = True

        if not is_invalid:
            try:
                current_user.add_class(year=year, semester=semester,
                                       class_name=class_name,
                                       building=building,
                                       start_time=start_time,
                                       end_time=end_time,
                                       week_days=''.join(week_days))
            except Exception as ex:
                pass

    return render_template("edit_schedule.html", form=tf,
                           cur_classes=sorted(current_user.all_classes(),
                                              key=lambda _: _.year + _.semester + str(_.start_time),
                                              reverse=True),
                           all_building_names=all_building_names)


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
    return render_template("settings.html",  form=form, title="password_change",
                           delete_account_form=delete_account_form, reset_account_form=reset_account_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/gmaps-redirect/<start_building_name>/<end_building_name>')
@login_required
def gmaps_redirect(start_building_name, end_building_name):
    graph = get_graph()
    loc1 = StudyInfo('00:00:00', '00:00:00', start_building_name)
    loc2 = StudyInfo('01:00:00', '00:00:00', end_building_name)
    paths = find_optimal_class_path(graph, [loc1, loc2])
    return redirect(path_to_gmaps_link(paths[0]))

