from flask import Flask, render_template, request, jsonify
from forms import ScheduleSearchForm, TestingForm, HittingForm, PitchingForm
import mlbapi
from hitting_everything2020 import hitting_everything2020
from pitching_everything2020 import pitching_everything2020
import selections

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

hit = {
        "P": selections.h_p_categories,
        "PG": selections.h_pg_categories,
        "Progressive": selections.h_p_categories,
        "Per Game": selections.h_pg_categories
    }

@app.route("/hitting", methods=["GET", "POST"])
def hitting():
    global form, selected, hit
    from hit import p2019, pg2019

    form = HittingForm()
    selected = "Progressive"
    form.category.choices= hit[selected]()

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        if types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year)
        if types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
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

#This route will return data back to the website w/e the user changes the select field
@app.route("/getdata/<types>")
def resend_selectionForm_data(types):
  print("The selected user from form:", types)

  global form,selected
  #user is the name of student sent back by fetch in javascript
  if types in hit:
    selected = types

    #the jsonify function is part of the Flask library and it needs to be imported
    return (jsonify( {"data": hit[types]()} ))
  else:
    return (jsonify({}) )

@app.route("/pitching", methods=["GET", "POST"])
def pitching():
    from pitch import p2019, pg2019

    form = PitchingForm()
    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
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

