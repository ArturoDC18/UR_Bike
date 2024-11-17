from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads

photos= UploadSet('photos', IMAGES)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PlaceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    picture = StringField('Picture URL')
    description = StringField('Description', validators=[DataRequired()])
    parking = BooleanField('Parking')
    repair = BooleanField('Repair')
    recommendation = BooleanField('Recommendation')
    submit = SubmitField('Add Place')
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(
            sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')