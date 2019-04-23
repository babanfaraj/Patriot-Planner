from python_src import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[Length(max=50), DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=25)],
                             widget=PasswordInput(hide_value=True))
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],
                                     widget=PasswordInput(hide_value=True))
    first_name = StringField('First Name', validators=[Length(max=25), DataRequired()])
    last_name = StringField('Last Name', validators=[Length(max=25), DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PasswordChange(FlaskForm):
    new_password = PasswordField('new_password', validators=[DataRequired()]);
    confirm_new_password = PasswordField('Confirm New Password',
                                         validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

class PasswordChange(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password',
                                         validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')


class DeleteAccount (FlaskForm):
    delete_account_confirmation=StringField('Delete Account Confirmation',validators=[DataRequired()])
    delete_btn = SubmitField('Delete Account')


class ResetAccount (FlaskForm):
    reset_account_confirmation = StringField('Reset Account Confirmation', validators=[DataRequired()])
    reset_btn = SubmitField('Reset Account')
