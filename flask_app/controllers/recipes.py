from flask_app import app, render_template, session, redirect,request
from flask_app.models.recipe import Recipe

@app.route("/recipes")
def recipes():
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("recipes.html")

@app.route("/recipes/new")
def show_recipe_form():
    return render_template("create.html")

@app.route("/recipes/new/add", methods=['post'])
def create_recipe():
    Recipe.save(request.form)
    return redirect("/recipes")
