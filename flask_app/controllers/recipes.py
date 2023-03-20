from flask_app import app, render_template, session, redirect,request
from flask_app.models.recipe import Recipe

@app.route("/recipes")
def recipes():
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("recipes.html",recipes = Recipe.get_all_recipes())

@app.route("/recipes/new")
def show_recipe_form():
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("create.html")

@app.route("/recipes/new/add", methods=['post'])
def create_recipe():
    print(request.form)
    if 'user_id' not in session:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    Recipe.save(request.form)
    return redirect("/recipes")

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect("/logout")
    session['recipe_id']=id
    recipe = Recipe.get_one(id)
    likers = Recipe.get_recipe_likers(id)
    
    return render_template("read_one.html",recipe=recipe, likers=likers)

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect("/logout")
    recipe = Recipe.get_one(id)
    return render_template("edit.html",recipe=recipe)


@app.route('/recipes/edit/update', methods=['post'])
def update_recipe():
    if 'user_id' not in session:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        print(request.form)

        return redirect(f"/recipes/edit/{request.form['id']}")
    Recipe.change(request.form)
    return redirect("/recipes")

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect("/logout")
    Recipe.delete(id)
    return redirect ("/recipes")





