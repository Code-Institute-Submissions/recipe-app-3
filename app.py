import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)



@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        if 'image' in request.files:
            image = request.files['image']
            if mongo.db.recipes.find_one({"img": image.filename}):
                image.filename = uuid.uuid4().hex[:6].upper()
            mongo.save_file(image.filename, image)
            recipe = {
                "name": request.form.get("name"),
                "recipe_category": request.form.get("recipe_category"),
                "diet_type": request.form.get("diet_type"),
                "ingredients": request.form.getlist('ingredient'),
                "cooking_directions": request.form.getlist('cooking_directions'),
                "link": request.form.get("link"),
                "img": image.filename
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe Successfully Added")
            return redirect(url_for('get_recipes'))
    categories = mongo.db.categories.find().sort("category_name", 1)
    diet_types = mongo.db.diet_types.find().sort("diet_name", 1)
    return render_template('add_recipe.html', categories=categories, diet_types=diet_types)


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)