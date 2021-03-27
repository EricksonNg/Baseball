from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from selections import hitter_names, pitcher_names, all_hitters, all_pitchers

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
    language = SelectField('Programming Language', choices=[('t', 'Test'), ('w', 'Working')], validators=[DataRequired()])
    submit = SubmitField("Submit")

class HittingForm(FlaskForm):
    year = SelectField("Year:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    types = SelectField("Category Type:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    types2 = SelectField("Category Type:", choices=[('Optional','Optional'),('Progressive', 'Progressive'), ('Per Game', 'Per Game')])
    category = SelectField("Category:", choices=[],validators=[DataRequired()])
    # category2 = StringField("Category:")
    category2 = SelectField("Category:", choices=[])
    player = SelectField("Player:", choices=[], validators=[DataRequired()])
    player2 = SelectField("Player 2: ", choices=[])
    team = SelectField("Team: ", choices = [('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'), ('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'), ('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'), ('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'), ('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'), ('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'), ('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    team2 = SelectField("Team: ", choices = [('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'), ('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'), ('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'), ('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'), ('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'), ('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'), ('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    # team = StringField("Team: ")
    submit = SubmitField("->")

class PitchingForm(FlaskForm):
    year = SelectField("Year:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    types = SelectField("Category Type:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    types2 = SelectField("Category Type:", choices=[('Optional', 'Optional'), ('Progressive', 'Progressive'), ('Per Game', 'Per Game')])
    category = SelectField("Category:", choices=[], validators=[DataRequired()])
    # category2 = StringField("Category:")
    category2 = SelectField("Category:", choices=[])
    player = SelectField("Player:", choices=[], validators=[DataRequired()])
    player2 = SelectField("Player 2: ", choices=[])
    team = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'),('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'),('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'),('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'),('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'),('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'),('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    team2 = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'),('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'),('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'),('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'),('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'),('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'),('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    submit = SubmitField("->")

class allChartsForm(FlaskForm):
    year = SelectField("Year:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    types = SelectField("Category Type:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    player = SelectField("Player:", choices=[], validators=[DataRequired()])
    team = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'),('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'),('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'),('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'),('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'),('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'),('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    submit = SubmitField("->")

class linescoreForm(FlaskForm):
    year = SelectField("Year:", choices=[('2020', '2020'), ('2019', '2019')], validators=[DataRequired()])
    player = SelectField("Player:", choices=[], validators=[DataRequired()])
    team = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BOS', 'BOS'),('CHC', 'CHC'), ('CIN', 'CIN'), ('CLE', 'CLE'), ('COL', 'COL'),('CWS', 'CWS'), ('DET', 'DET'), ('HOU', 'HOU'), ('KC', 'KC'), ('LAA', 'LAA'),('LAD', 'LAD'), ('MIA', 'MIA'), ('MIL', 'MIL'), ('MIN', 'MIN'),('NYM', 'NYM'), ('NYY', 'NYY'), ('OAK', 'OAK'), ('PHI', 'PHI'),('PIT', 'PIT'), ('SD', 'SD'), ('SEA', 'SEA'), ('STL', 'STL'), ('TB', 'TB'),('TEX', 'TEX'), ('TOR', 'TOR'), ('WSH', 'WSH')])
    submit = SubmitField("->")