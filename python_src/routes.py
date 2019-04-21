from python_src import app
from flask import render_template, flash, redirect, url_for
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

    if form.validate_on_submit():
        # Iterate through database until current user is reached
        # Change users password
        flash('Password Changed', 'success')
        print(form.new_password.data)
        print(form.confirm_new_password.data)

    return render_template("settings.html", form=form, title="password_change")



