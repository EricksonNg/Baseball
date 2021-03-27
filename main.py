from flask import Flask, render_template, request, jsonify
from forms import ScheduleSearchForm, TestingForm, HittingForm, PitchingForm, allChartsForm, linescoreForm
import mlbapi
# from standings import standings
import selections
import git

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
    return render_template("about.html")

@app.route("/charts", methods= ["GET", "POST"])
def charts():
    from hit2021 import getID
    from allPitchData import pitchCharts
    # id = getID("Mike Yastrzemski", "2020", "SF")
    # link = "https://img.mlbstaticage/upload/w_426,q_10v1/people/" + id + "/headshot/67/current"

    pitchName, pitchAmount = pitchCharts("Drew Smyly", "SF", "Lefties")
    print(pitchName, pitchAmount)

    return render_template("charts.html", pitchName = pitchName, pitchAmount = pitchAmount)

hit = {
    "P": selections.h_p_categories,
    "PG": selections.h_pg_categories,
    "Progressive": selections.h_p_categories,
    "Per Game": selections.h_pg_categories,
    "Optional": selections.h_p_categories
}

pitch = {
    "P": selections.p_p_categories,
    "PG": selections.p_pg_categories,
    "Progressive": selections.p_p_categories,
    "Per Game": selections.p_pg_categories,
    "Optional": selections.p_p_categories
}

year = "2020" # Gives a default value for year (having a year variable specified here allows for only one all_hitters and all_pitchers function (both in selections.py) to ever be needed when there will be different years)
selected = "Progressive"  # Do not put inside the the function where "selected" is called (it will cause the selectfield to go back to the choices for "Progressive" after submitting)
selected2 = "Optional"
team = "SF"
print("Team is SF")
team2 = "SF"
print("Team2 is SF")
page = "hitting"  # giving page a default value (doesn't really affect anything)

@app.route("/hitting", methods=["GET", "POST"])
def hitting():
    from hit2021 import p, pg
    global page, selected, selected2, team, team2, year
    print("1", team, team2)

    if page != "hitting":
        print("Page wasn't \"Hitting\"")
        year = "2020"
        selected = "Progressive"  # changes dynamic selectfield back to the progressive choices after page change
        selected2 = "Optional"
        team = "SF"
        team2 = "SF"
        category2 = 'Optional'
    page = "hitting"  # helps differentiate hitting and pitching category choices in resend_selectionForm_data function

    print("2", team, team2)

    print("Making forms")
    form = HittingForm()
    form.category.choices = hit[selected]()
    form.category2.choices = hit[selected2]()
    form.player.choices = selections.all_hitters(team, year)
    form.player2.choices = selections.all_hitters(team2, year)
    print("Forms should be done")

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        types2 = request.form.to_dict(flat=False)["types2"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        playername2 = request.form.to_dict(flat=False)["player2"][0]
        team = request.form.to_dict(flat=False)["team"][0]
        team2 = request.form.to_dict(flat=False)["team2"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        category2 = request.form.to_dict(flat=False)["category2"][0]
        if 'Select A Player' in playername:
            print("A player is not selected at all")
            a = None
            b = None
            c = None
            d = None
            e = None
            f = None
        elif types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p(playername, category, year, team)
        elif types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
            a, b, c = pg(playername, category, year, team)

        if 'Select A Player' in playername2:
            print("1: A player is not selected for the second player form")
            playername2 = playername
        if types2 == 'Optional':
            print("The second types form is empty")
            d = None
            e = None
            f = None
        elif types2 == 'P' or types2 == 'progressive' or types2 == 'Progressive':
            f, d, e = p(playername2, category2, year, team2)
        elif types2 == 'PG' or types2 == 'per game' or types2 == 'Per Game':
            f, d, e = pg(playername2, category2, year, team2)

        return render_template(
            "hitting.html", F=form,
            player_date=a,
            player_date2=f,
            player_category=b,
            category=c,
            player_category2=d,
            category2=e,
            player_name=playername)

    return render_template(
        "hitting.html",
        F=form)

@app.route("/pitching", methods=["GET", "POST"])
def pitching():
    from pitch2021 import p, pg
    global page, selected, selected2, team, team2, year
    print("3", team, team2)

    if page != "pitching":
        print("Page wasn't \"Pitching\"")
        year = "2020"
        selected = "Progressive"  # changes dynamic selectfield back to the progressive choices after page change
        selected2 = "Optional"
        team = "SF"
        team2 = "SF"
        category2 = 'Optional'
    print("4", team, team2)

    page = "pitching"  # helps differentiate hitting and pitching category choices in resend_selectionForm_data function

    print("Making forms")
    form = PitchingForm()
    form.category.choices = pitch[selected]()
    form.category2.choices = pitch[selected2]()
    form.player.choices = selections.all_pitchers(team, year)
    form.player2.choices = selections.all_pitchers(team2, year)
    print("Forms should be finished")

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        types2 = request.form.to_dict(flat=False)["types2"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        playername2 = request.form.to_dict(flat=False)["player2"][0]
        team = request.form.to_dict(flat=False)["team"][0]
        team2 = request.form.to_dict(flat=False)["team2"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        category2 = request.form.to_dict(flat=False)["category2"][0]
        if 'Select A Player' in playername2:
            print("1: A player is not selected for the second player form")
            playername2 = playername
        if 'Select A Player' in playername:
            print("A player is not selected at all")
            a = None
            b = None
            c = None
            d = None
            e = None
            f = None
        elif types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p(playername, category, year, team)
        elif types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
            a, b, c = pg(playername, category, year, team)
        if 'Select A Player' in playername:
            print("2: A player is not selected for the second player form")
            a = None
            b = None
            c = None
            d = None
            e = None
            f = None
        if category2 == '':
            print("The second category form is empty")
            d = None
            e = None
            f = None
        elif types2 == 'Optional':
            print("The second types form is empty")
            d = None
            e = None
            f = None
        elif types2 == 'P' or types2 == 'progressive' or types2 == 'Progressive':
            f, d, e = p(playername2, category2, year, team2)
        elif types2 == 'PG' or types2 == 'per game' or types2 == 'Per Game':
            f, d, e = pg(playername2, category2, year, team2)

        return render_template(
            "pitching.html", F=form,
            player_date=a,
            player_date2=f,
            player_category=b,
            category=c,
            player_category2=d,
            category2=e,
            player_name=playername)

    return render_template(
        "pitching.html",
        F=form)

# @app.route("/fielding", methods=["GET", "POST"])
# def fielding():

@app.route('/all-charts', methods=["GET", "POST"])
def allCharts():
    global team, year
    from allCategories import all, allChartsPG

    form = allChartsForm()
    form.player.choices = selections.all_hitters(team, year)
    playername = None # Setting playername as None here allows for the div where all the charts to show up only after the forms are submitted (so there won't be an empty outline)

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        team = request.form.to_dict(flat=False)["team"][0]
        if types == "Progressive":
            allStats, dates = all(team, year, playername)
        if types == "Per Game":
            allStats, dates = allChartsPG(team, year, playername)

        return render_template("allCharts.html", F = form, range=range, len=len, dates=dates, allStats=allStats, playername=playername, type = types)

    return render_template(
        "allCharts.html", F = form)

@app.route('/linescore', methods=["GET", "POST"])
def linescore():
    global team, year
    from allCategories import allpg, allp

    form = linescoreForm()
    form.player.choices = selections.all_hitters(team, year)
    playername = None # Setting playername as None here allows for the div where all the charts to show up only after the forms are submitted (so there won't be an empty outline)

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        team = request.form.to_dict(flat=False)["team"][0]
        perGameData, dates, order, positions = allpg(team, year, playername)
        progressionData, seasonOrder = allp(team, year, playername)

        return render_template("linescore.html", F = form, range= range, len= len, perGameData = perGameData, playername=playername, order = order, positions = positions, dates = dates, progressionData = progressionData, seasonOrder = seasonOrder)

    return render_template(
        "linescore.html", F = form)

#first category form
@app.route("/getdata/<types>")
def resend_selectionForm_data(types):
    global form, selected, page
    print("The selected user from form 1:", types)

    # user is the name of student sent back by fetch in javascript
    if page == "hitting":
        if types in hit:
            selected = types
            print("This means that selected from form 1 now is:", selected)

            # the jsonify function is part of the Flask library and it needs to be imported
            return (jsonify({"data": hit[types]()}))
        else:
            return (jsonify({}))
    elif page == "pitching":
        if types in pitch:
            selected = types

            return (jsonify({"data": pitch[types]()}))
        else:
            return (jsonify({}))

#second category form
@app.route("/getdata2/<types>")
def resend_selectionForm_data2(types):
    global form, selected2, page
    print("The selected user from form 2:", types)

    # user is the name of student sent back by fetch in javascript
    if page == "hitting":
        if types in hit:
            selected2 = types
            print("This means that selected now is:", selected2)

            # the jsonify function is part of the Flask library and it needs to be imported
            return (jsonify({"data": hit[types]()}))
        else:
            return (jsonify({}))
    elif page == "pitching":
        if types in pitch:
            selected2 = types

            return (jsonify({"data": pitch[types]()}))
        else:
            return (jsonify({}))

#first team form
@app.route("/getdata3/<types>")
def resend_selectionForm_data3(types):
    global form, team, page, year
    print("The team from form:", types)

    if page == "hitting":
        team = types
        print("This means that team now is:", team)

        # the jsonify function is part of the Flask library and it needs to be imported
        return (jsonify({"data": selections.all_hitters(team, year)}))
    elif page == "pitching":
        team = types
        print("This means that team now is:", team)

        return (jsonify({"data": selections.all_pitchers(team, year)}))

#second team form
@app.route("/getdata4/<types>")
def resend_selectionForm_data4(types):
    global form, team2, page, year
    print("The team from form:", types)

    if page == "hitting":
        team2 = types
        print("This means that team now is:", team2)

        # the jsonify function is part of the Flask library and it needs to be imported
        return (jsonify({"data": selections.all_hitters(team2, year)}))
    elif page == "pitching":
        team2 = types
        print("This means that team now is:", team2)

        return (jsonify({"data": selections.all_pitchers(team2, year)}))

#year form (this one is for the first player form)
@app.route("/getdata5/<types>")
def resend_selectionForm_data5(types):
    global form, team, page, year
    print("The year form:", types)

    if page == "hitting":
        year = types
        print("This means that year now is:", year)

        # the jsonify function is part of the Flask library and it needs to be imported
        return (jsonify({"data": selections.all_hitters(team, year)}))
    elif page == "pitching":
        year = types
        print("This means that year now is:", year)

        return (jsonify({"data": selections.all_pitchers(team, year)}))

#year form (this one is for the second player form)
@app.route("/getdata6/<types>")
def resend_selectionForm_data6(types):
    global form, team2, page, year
    print("The year form:", types)

    if page == "hitting":
        year = types
        print("This means that year now is:", year)

        # the jsonify function is part of the Flask library and it needs to be imported
        return (jsonify({"data": selections.all_hitters(team2, year)}))
    elif page == "pitching":
        year = types
        print("This means that year now is:", year)

        return (jsonify({"data": selections.all_pitchers(team2, year)}))

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


@app.route('/129521update', methods=['POST'])
def webhook():
    print("Linked reached")
    if request.method == 'POST':
        print("POSTED")
        repo = git.Repo('https://github.com/EricksonNg/Baseball.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

try:
    app.run(debug=True, use_reloader=False)
except Exception as e:
    print(e)
