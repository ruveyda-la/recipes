from flask_app import app, render_template, session, redirect,request
from flask_app.models.like import Like

@app.route('/recipe/like/<int:recipe_id>')
def like_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect("/logout")
    recipe_id = session['recipe_id']

    Like.save_like()
        
    return redirect(f"/recipes/{recipe_id}")

