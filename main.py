from flask import Flask, render_template, request, jsonify
from forms import ScheduleSearchForm, TestingForm, HittingForm, PitchingForm
import mlbapi
from hitting_everything2020 import hitting_everything2020
from pitching_everything2020 import pitching_everything2020
# from standings import standings
import selections
import git

try:
    hitting_everything2020()
    pitching_everything2020()
except Exception as e:
    print(e)

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

hit = {
    "P": selections.h_p_categories,
    "PG": selections.h_pg_categories,
    "Progressive": selections.h_p_categories,
    "Per Game": selections.h_pg_categories
}

pitch = {
    "P": selections.p_p_categories,
    "PG": selections.p_pg_categories,
    "Progressive": selections.p_p_categories,
    "Per Game": selections.p_pg_categories
}

selected = "Progressive"  # Do not put inside the the function where "selected" is called (it will cause the selectfield to go back to the choices for "Progressive" after submitting)
page = "hitting"  # giving page a default value (doesn't really affect anything)


@app.route("/hitting", methods=["GET", "POST"])
def hitting():
    from hit import p2019, pg2019
    global page, selected

    if page != "hitting":
        selected = "Progressive"  # changes dynamic selectfield back to the progressive choices after page change
    page = "hitting"  # helps differentiate hitting and pitching category choices in resend_selectionForm_data function
    form = HittingForm()
    form.category.choices = hit[selected]()

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        if playername == 'Select A Player':
            a = None
            b = None
            c = None
        elif types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year)
        elif types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
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
    global page, selected

    if page != "pitching":
        selected = "Progressive"  # changes dynamic selectfield back to the progressive choices after page change
    page = "pitching"  # helps differentiate hitting and pitching category choices in resend_selectionForm_data function
    form = PitchingForm()
    form.category.choices = pitch[selected]()

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        if types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year)
        elif types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
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


# This route will return data back to the website w/e the user changes the select field
@app.route("/getdata/<types>")
def resend_selectionForm_data(types):
    global form, selected, page
    print("The selected user from form:", types)

    # user is the name of student sent back by fetch in javascript
    if page == "hitting":
        if types in hit:
            selected = types
            print("This means that selected now is:", selected)

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
    if request.method == 'POST':
        repo = git.Repo('https://github.com/EricksonNg/Baseball.git')
        origin = repo.remotes.origin
    origin.pull()

try:
    app.run(debug=True, use_reloader=False)
except Exception as e:
    print(e)
