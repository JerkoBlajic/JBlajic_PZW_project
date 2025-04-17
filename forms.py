from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, FileField, SubmitField, RadioField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime
from flask_wtf.file import FileAllowed

class FoodPostForm(FlaskForm):
    title = StringField('Dish Name', validators=[DataRequired(), Length(min=5, max=100)])  # Capitalized 'Name'
    content = TextAreaField('Dish Description', render_kw={"id": "markdown-editor"})  # Capitalized 'Description'
    date = DateField('Date', default=datetime.today)
    status = RadioField('Status', choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')  # Corrected 'Skica' and 'Objavljeno' to English
    image = FileField('Food Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])  # Corrected 'Samo slike!'
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])  # Changed 'E-mail' to 'Email' for consistency
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Stay Logged In')  # Capitalized 'Logged In'
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    restaurant_name = StringField('Restaurant Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):
    restaurant_name = StringField("Restaurant Name", validators=[DataRequired(), Length(max=50)])
    address = StringField("Address", validators=[DataRequired(), Length(max=50)])
    bio = TextAreaField("Bio", validators=[Length(max=1000)], render_kw={"id": "markdown-editor"})
    theme = SelectField('Theme', choices=[
        ('', ''),
        ('cerulean', 'Cerulean'),
        ('cosmo', 'Cosmo'),
        ('cyborg', 'Cyborg'),
        ('darkly', 'Darkly'),
        ('flatly', 'Flatly'),
        ('journal', 'Journal'),
        ('litera', 'Litera'),
        ('lumen', 'Lumen'),
        ('lux', 'Lux'),
        ('materia', 'Materia'),
        ('minty', 'Minty'),
        ('morph', 'Morph'),
        ('pulse', 'Pulse'),
        ('quartz', 'Quartz'),
        ('sandstone', 'Sandstone'),
        ('simplex', 'Simplex'),
        ('sketchy', 'Sketchy'),
        ('slate', 'Slate'),
        ('solar', 'Solar'),
        ('spacelab', 'Spacelab'),
        ('superhero', 'Superhero'),
        ('united', 'United'),
        ('vapor', 'Vapor'),
        ('yeti', 'Yeti'),
        ('zephyr', 'Zephyr')
    ])
    image = FileField('Your Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    submit = SubmitField("Save")

class UserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(3, 64), Email()])
    restaurant_name = StringField("Restaurant Name", validators=[DataRequired(), Length(max=50)])
    address = StringField("Address", validators=[DataRequired(), Length(max=50)])
    is_confirmed = BooleanField('Confirmed')
    bio = TextAreaField("Bio", validators=[Length(max=1000)], render_kw={"id": "markdown-editor"})
    theme = SelectField('Theme', choices=[
        ('', ''),
        ('cerulean', 'Cerulean'),
        ('cosmo', 'Cosmo'),
        ('cyborg', 'Cyborg'),
        ('darkly', 'Darkly'),
        ('flatly', 'Flatly'),
        ('journal', 'Journal'),
        ('litera', 'Litera'),
        ('lumen', 'Lumen'),
        ('lux', 'Lux'),
        ('materia', 'Materia'),
        ('minty', 'Minty'),
        ('morph', 'Morph'),
        ('pulse', 'Pulse'),
        ('quartz', 'Quartz'),
        ('sandstone', 'Sandstone'),
        ('simplex', 'Simplex'),
        ('sketchy', 'Sketchy'),
        ('slate', 'Slate'),
        ('solar', 'Solar'),
        ('spacelab', 'Spacelab'),
        ('superhero', 'Superhero'),
        ('united', 'United'),
        ('vapor', 'Vapor'),
        ('yeti', 'Yeti'),
        ('zephyr', 'Zephyr')
    ])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    submit = SubmitField("Save")