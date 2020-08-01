from flask import Flask, render_template, request
from forms import ScheduleSearchForm, PlayerSearchForm, TestingForm
import mlbapi
from hitting_everything2020 import hitting_everything2020
from pitching_everything2020 import pitching_everything2020

hitting_everything2020()
pitching_everything2020()

app = Flask('app')
app.config["SECRET_KEY"] = "1234"

# Python decorator
@app.route('/')
@app.route('/home')
# routes us to home page whenever a user visit the site
def homepage():
    return render_template(
        "index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    form = TestingForm()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=False)["language"][0]
        print(data)
    return render_template("about.html", F = form)

@app.route("/hitting", methods=["GET", "POST"])
def hitting():
    from hit import p2019, pg2019
    form = PlayerSearchForm()
    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["name"][0]
        # if types == 'Progressive':
        #     category = request.form.to_dict(flat=False)["h_p_category"][0]
        # if types == 'Per Game':
        #     category = request.form.to_dict(flat=False)["h_pg_category"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        if types == 'p' or types == 'progressive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year)
        if types == 'pg' or types == 'per game' or types == 'Per game' or types == 'Per Game':
            a, b, c = pg2019(playername, category, year)

        return render_template(
            "hitting.html", F=form,
            player_date=a,
            player_category=b,
            category=c,
            player_name=playername)

    return render_template(
        "hitting.html",
        F=form)


@app.route("/pitching", methods=["GET", "POST"])
def pitching():
    from pitch import p2019, pg2019

    form = PlayerSearchForm()
    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["name"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        if types == 'p' or types == 'progresive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year)
        if types == 'pg' or types == 'per game' or types == 'Per game' or types == 'Per Game':
            a, b, c = pg2019(playername, category, year)

        return render_template(
            "pitching.html", F=form,
            player_date=a,
            player_category=b,
            category=c,
            player_name=playername)

    return render_template(
        "pitching.html",
        F=form)


@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    form = ScheduleSearchForm()
    if form.validate_on_submit():
        # Get the user's input data, and use it as a parameter for the api call
        start_date = request.form.to_dict(flat=False)["start"][0]
        end_date = request.form.to_dict(flat=False)["end"][0]
        game_info = mlbapi.search_sched(start_date, end_date)
        win = mlbapi.pbp()
        return render_template("schedule.html", F=form, data=game_info, win_p=win)

    return render_template(
        "schedule.html",
        F=form)


app.run(debug=True, use_reloader=False)

# @app.route("/hitting_p", methods = ["GET", "POST"])
# def hitting_p():
#   from hit2019 import p2019

#   form = PlayerSearchForm()
#   if form.validate_on_submit():
#     print("POST REQUEST COMPLETED!")
#     playername = request.form.to_dict(flat = False)["name"][0]
#     category = request.form.to_dict(flat=False)["category"][0]
#     a,b,c = p2019(playername, category)

#     return render_template(
#       "hitting_p.html", F = form, 
#       player_date = a, 
#       player_category = b, 
#       category = c,
#       player_name = playername)

#   return render_template(
#     "hitting_p.html", 
#     F = form)

# @app.route("/hitting_pg", methods = ["GET", "POST"])
# def hitting_pg():
#   from hit2019 import pg2019

#   form = PlayerSearchForm()
#   if form.validate_on_submit():
#     print("POST REQUEST COMPLETED!")
#     playername = request.form.to_dict(flat = False)["name"][0]
#     category = request.form.to_dict(flat=False)["category"][0]
#     a,b,c = pg2019(playername, category)

#     return render_template(
#       "hitting_pg.html", F = form, 
#       player_date = a, 
#       player_category = b, 
#       category = c,
#       player_name = playername)

#   return render_template(
#     "hitting_pg.html", 
#     F = form)

# @app.route("/pitching_p", methods = ["GET", "POST"])
# def pitching_p():
#   from pitch2019 import p2019

#   form = PlayerSearchForm()
#   if form.validate_on_submit():
#     print("POST REQUEST COMPLETED!")
#     playername = request.form.to_dict(flat = False)["name"][0]
#     category = request.form.to_dict(flat=False)["category"][0]
#     a,b,c = p2019(playername, category)

#     return render_template(
#       "pitching_p.html", F = form, 
#       player_date = a, 
#       player_category = b, 
#       category = c,
#       player_name = playername)

#   return render_template(
#     "pitching_p.html", 
#     F = form)

# @app.route("/pitching_pg", methods = ["GET", "POST"])
# def pitching_pg():
#   from pitch2019 import pg2019

#   form = PlayerSearchForm()
#   if form.validate_on_submit():
#     print("POST REQUEST COMPLETED!")
#     playername = request.form.to_dict(flat = False)["name"][0]
#     category = request.form.to_dict(flat=False)["category"][0]
#     a,b,c = pg2019(playername, category)

#     return render_template(
#       "pitching_pg.html", F = form, 
#       player_date = a, 
#       player_category = b, 
#       category = c,
#       player_name = playername)

#   return render_template(
#     "pitching_pg.html", 
#     F = form)
