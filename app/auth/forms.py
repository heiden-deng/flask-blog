from flask_wtf import Form,FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo,DataRequired
from wtforms import ValidationError
from ..models import User
from ..email import send_email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    username = StringField('username', validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                  'Usernames must have only letters, '
                                                                                  'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password',validators=[DataRequired()])
    password = PasswordField('New Password',validators=[DataRequired(),EqualTo('password2','Password must match')])
    password2 = PasswordField('Confirm new Password',validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')