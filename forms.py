from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TeamSearchForm(FlaskForm):
  name = StringField("Team name: ", validators = [ DataRequired()])
  #search bar for stat page
  submit = SubmitField("Find") # the parameter is the label on the button

class ScheduleSearchForm(FlaskForm):
  start = StringField("Start Date: ", validators = [ DataRequired()])
  end = StringField("End Date: ", validators = [ DataRequired()])
  #search bar for schedule page
  submit = SubmitField("Find") # the parameter is the label on the button

class PlayerSearchForm(FlaskForm):
  types= StringField("T:", validators = [ DataRequired()])
  name = StringField("N:", validators = [ DataRequired()])
  category = StringField("C:", validators = [ DataRequired()])
  category2 = StringField("Category 2: ")
  category3 = StringField("Category 3: ")
  #search bar for stats page
  submit = SubmitField("Find") # the parameter is the label on the button