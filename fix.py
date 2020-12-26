@app.route("/hitting", methods=["GET", "POST"])
def hitting():
    from hit import p2019, pg2019
    global page, selected, selected2, team, team2, category2

    #if user were on a page other than the "Hitting" page, this if statement makes it so that the different fields should revert back to their default values if they were changed on a different page
    if page != "hitting":
        selected = "Progressive"
        selected2 = "Optional"
        team = "SF"
        category2 = 'Optional'

    page = "hitting"  # helps differentiate hitting and pitching category choices in resend_selectionForm_data function

    form = HittingForm() # assigning HittingForm function from Forms.py to the variable "form" to easily access the function

    form.category.choices = hit[selected]() # first category field choices (orginially left blank in HittingForms()) assigned depending on what selected is (refers to the dictionary "hit")

    form.category2.choices = hit[selected2]() # second category field choices (orginially left blank in HittingForms()) assigned depending on what selected is (refers to the dictionary "hit")

    form.player.choices = selections.all_hitters(team) # refers to all_hitters() function in selections.py to fill the first player field (choices originally left blank in HittingForm())

    form.player2.choices = selections.all_hitters(team2) # refers to all_hitters() function in selections.py to fill the second player field (choices originally left blank in HittingForm())

    if form.validate_on_submit():
        print("POST REQUEST COMPLETED!")
        # Using form.to_dict to get the data from the different fields in HittingForm()/form and assigning the data to the same variable name as it was there
        year = request.form.to_dict(flat=False)["year"][0]
        types = request.form.to_dict(flat=False)["types"][0]
        types2 = request.form.to_dict(flat=False)["types2"][0]
        playername = request.form.to_dict(flat=False)["player"][0]
        playername2 = request.form.to_dict(flat=False)["player2"][0]
        team = request.form.to_dict(flat=False)["team"][0]
        team2 = request.form.to_dict(flat=False)["team2"][0]
        category = request.form.to_dict(flat=False)["category"][0]
        category2 = request.form.to_dict(flat=False)["category2"][0]

        # If second player name field has 'Select A Player' in it's input, playername2 will be the same as the name in the first player name field (useful if user wants to see 2 charts from the same player)
        if 'Select A Player' in playername2:
            playername2 = playername

        # Makes sure that no error will come up if the first player name field is left as 'Select A Player'
        if 'Select A Player' in playername:
            a = None
            b = None
            c = None
            d = None
            e = None
            f = None

        # Assigns values to a (list of dates player played), b (list of the stats), and c (title for the chart) by using return values from functions in hit.py (if category type is Progressive, p2019 is used, and if the category types is Per Game, then pg2019 is used)
        elif types == 'P' or types == 'progressive' or types == 'Progressive':
            a, b, c = p2019(playername, category, year, team)
        elif types == 'PG' or types == 'per game' or types == 'Per game' or types == 'Per Game':
            a, b, c = pg2019(playername, category, year, team)

        # Assigns values to f (list of dates player played), d (list of the stats), and e (title for the chart) by using return values from functions in hit.py (if category type is Progressive, p2019 is used, and if the category types is Per Game, then pg2019 is used)
        elif types2 == 'P' or types2 == 'progressive' or types2 == 'Progressive':
            f, d, e = p2019(playername2, category2, year, team2)
        elif types2 == 'PG' or types2 == 'per game' or types2 == 'Per Game':
            f, d, e = pg2019(playername2, category2, year, team2)

        if 'Select A Player' in playername:
            a = None
            b = None
            c = None
            d = None
            e = None
            f = None
        if types2 == 'Optional':
            d = None
            e = None
            f = None
        if 'Select A Player' in playername2:
            d = None
            e = None
            f = None
        elif category2 == '':
            d = None
            e = None
            f = None


        return render_template(
            "hitting.html", F=form,
            player_date=a,
            player_date2 = f,
            player_category=b,
            category=c,
            player_category2 = d,
            category2 = e,
            player_name=playername)

    return render_template(
        "hitting.html",
        F=form)