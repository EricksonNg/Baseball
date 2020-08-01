from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from selections import names
import selections

class TeamSearchForm(FlaskForm):
    name = StringField("Team name: ", validators=[DataRequired()])
    # search bar for stat page
    submit = SubmitField("Find")  # the parameter is the label on the button

class ScheduleSearchForm(FlaskForm):
    start = StringField("Start Date: ", validators=[DataRequired()])
    end = StringField("End Date: ", validators=[DataRequired()])
    # search bar for schedule page
    submit = SubmitField("Find")  # the parameter is the label on the button

class PlayerSearchForm(FlaskForm):
    year = SelectField("Year:", choices = [('2020','2020'),('2019','2019')], validators=[DataRequired()])
    types = SelectField("Type:", choices = [('Progressive','Progressive'),('Per Game','Per Game')], validators=[DataRequired()])
    name = StringField("N:", validators=[DataRequired()])
    h_p_category = SelectField("Type:", choices = selections.h_p_categories(), validators=[DataRequired()])
    h_pg_category = SelectField("Type:", choices = selections.h_pg_categories(), validators=[DataRequired()])
    p_p_category = SelectField("Type:", choices = selections.p_p_categories(), validators=[DataRequired()])
    p_pg_category = SelectField("Type:", choices = selections.p_pg_categories(), validators=[DataRequired()])
    category = StringField("C:", validators=[DataRequired()])
    # search bar for stats page
    submit = SubmitField("Find")  # the parameter is the label on the button

# class TestingForm(FlaskForm):
#     language = SelectField('Programming Language',
#                            choices=[('cpp', "name1"), ('py', 'Python'), ('text', 'Plain Text')],
#                            validators=[DataRequired()])
#     submit = SubmitField("Submit")

class TestingForm(FlaskForm):
    language = SelectField('Programming Language',
                           choices=names(),
                           validators=[DataRequired()])
    submit = SubmitField("Submit")

