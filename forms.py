from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from selections import hitter_names, pitcher_names
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

class TestingForm(FlaskForm):
    language = SelectField('Programming Language',
                           choices=[('t', 'Test'), ('w', 'Working')],
                           validators=[DataRequired()])
    submit = SubmitField("Submit")

class HittingForm(FlaskForm):
    year = SelectField("Y:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    types = SelectField("T:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    category = StringField("C:", validators=[DataRequired()])
    # category = SelectField("C:", choices=[('Average', 'Average'), ('On Base Percentage', 'On Base Percentage'), ('Slugging', 'Slugging'), ('On Base Plus Slugging', 'On Base Plus Slugging'), ('Runs', 'Runs'), ('Doubles', 'Doubles'), ('Triples', 'Triples'), ('Home Runs', 'Home Runs'), ('Strikeouts', 'Strikeouts'), ('Walks', 'Walks'), ('Hits', 'Hits'), ('At Bats', 'At Bats'), ('Stolen Bases', 'Stolen Bases'), ('Stolen Bases', 'Stolen Bases'), ('Runs Batted In', 'Runs Batted In'), ('Left On Base', 'Left On Base'), ('At Bats', 'At Bats'), ('Strikeouts', 'Strikeouts'), ('Hits', 'Hits'), ('Walks', 'Walks'), ('Runs', 'Runs'), ('Runs Batted In', 'Runs Batted In'), ('Stolen Bases', 'Stolen Bases'), ('Left On Base', 'Left On Base'), ('Doubles', 'Doubles'), ('Triples', 'Triples'), ('Home Runs', 'Home Runs')], validators=[DataRequired()])
    # h_p_category = SelectField("Type:", choices = selections.h_p_categories(), validators=[DataRequired()])
    # h_pg_category = SelectField("Type:", choices = selections.h_pg_categories(), validators=[DataRequired()])
    player = SelectField("P:",
                         choices=hitter_names(),
                         validators=[DataRequired()])
    submit = SubmitField("->")

class PitchingForm(FlaskForm):
    year = SelectField("Y:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    types = SelectField("T:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    category = StringField("C:", validators=[DataRequired()])
    # p_p_category = SelectField("Type:", choices = selections.p_p_categories(), validators=[DataRequired()])
    # p_pg_category = SelectField("Type:", choices = selections.p_pg_categories(), validators=[DataRequired()])
    player = SelectField("P:",
                         choices=pitcher_names(),
                         validators=[DataRequired()])
    submit = SubmitField("->")
