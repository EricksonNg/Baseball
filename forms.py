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
    team = SelectField("Team: ", choices = [('SF','SF'),('ARI','ARI'),('COL','COL'),('LAD','LAD'),('SD','SD'),('CHC','CHC'),('CIN','CIN'),('MIL','MIL'),('PIT','PIT'),('STL','STL'),('ATL','ATL'),('MIA','MIA'),('NYM','NYM'),('PHI','PHI'),('WSH','WSH'),('HOU','HOU'),('LAA','LAA'),('OAK','OAK'),('SEA','SEA'),('TEX','TEX'),('CWS','CWS'),('CLE','CLE'),('DET','DET'),('KC','KC'),('MIN','MIN'),('BAL','BAL'),('BOS','BOS'),('NYY','NYY'),('TB','TB'),('TOR','TOR')])
    team2 = SelectField("Team: ", choices = [('SF','SF'),('ARI','ARI'),('COL','COL'),('LAD','LAD'),('SD','SD'),('CHC','CHC'),('CIN','CIN'),('MIL','MIL'),('PIT','PIT'),('STL','STL'),('ATL','ATL'),('MIA','MIA'),('NYM','NYM'),('PHI','PHI'),('WSH','WSH'),('HOU','HOU'),('LAA','LAA'),('OAK','OAK'),('SEA','SEA'),('TEX','TEX'),('CWS','CWS'),('CLE','CLE'),('DET','DET'),('KC','KC'),('MIN','MIN'),('BAL','BAL'),('BOS','BOS'),('NYY','NYY'),('TB','TB'),('TOR','TOR')])
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
    team = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('COL', 'COL'), ('LAD', 'LAD'), ('SD', 'SD'), ('CHC', 'CHC'), ('CIN', 'CIN'), ('MIL', 'MIL'), ('PIT', 'PIT'), ('STL', 'STL'), ('ATL', 'ATL'), ('MIA', 'MIA'), ('NYM', 'NYM'), ('PHI', 'PHI'), ('WSH', 'WSH'), ('HOU', 'HOU'), ('LAA', 'LAA'), ('OAK', 'OAK'), ('SEA', 'SEA'), ('TEX', 'TEX'), ('CWS', 'CWS'), ('CLE', 'CLE'), ('DET', 'DET'), ('KC', 'KC'), ('MIN', 'MIN'), ('BAL','BAL'), ('BOS', 'BOS'), ('NYY', 'NYY'), ('TB', 'TB'), ('TOR', 'TOR')])
    team2 = SelectField("Team: ", choices=[('SF', 'SF'), ('ARI', 'ARI'), ('COL', 'COL'), ('LAD', 'LAD'), ('SD', 'SD'), ('CHC', 'CHC'), ('CIN', 'CIN'), ('MIL', 'MIL'), ('PIT', 'PIT'), ('STL', 'STL'), ('ATL', 'ATL'), ('MIA', 'MIA'), ('NYM', 'NYM'), ('PHI', 'PHI'), ('WSH', 'WSH'), ('HOU', 'HOU'), ('LAA', 'LAA'), ('OAK', 'OAK'), ('SEA', 'SEA'), ('TEX', 'TEX'), ('CWS', 'CWS'), ('CLE', 'CLE'), ('DET', 'DET'), ('KC', 'KC'), ('MIN', 'MIN'), ('BAL', 'BAL'), ('BOS', 'BOS'), ('NYY', 'NYY'), ('TB', 'TB'), ('TOR', 'TOR')])
    submit = SubmitField("->")
