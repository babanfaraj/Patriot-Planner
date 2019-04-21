from python_src import app
from flask import render_template
from python_src.forms import PasswordChange

@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    return render_template("index.html")


@app.route('/home')
def about():
    return render_template("home.html")


@app.route('/new_route')
def new_route():
    return render_template("new_route.html")


@app.route('/edit_schedule')
def blog():
    return render_template("edit_schedule.html")


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = PasswordChange()
    return render_template("settings.html", title='Settings', form=form)



