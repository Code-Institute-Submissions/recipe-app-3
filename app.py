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


#Home route

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


#Route to add a newcrecipe

@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        if 'image' in request.files:
            image = request.files['image']
            #Rename the image to a random string if the name already exists in the database:
            if mongo.db.recipes.find_one({"img": image.filename}):
                image.filename = uuid.uuid4().hex[:6].upper()
            mongo.save_file(image.filename, image)
            recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_category": request.form.get("recipe_category"),
                "diet_type": request.form.getlist("diet_type"),
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


#Route to update a recipe

@app.route('/edit_recipe/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        #only update image if the user chose a new image, otherwise don't update
        if 'image' in request.files:
            image = request.files['image']
            #Rename the image to a random string if the name already exists in the database:
            if mongo.db.recipes.find_one({"img": image.filename}):
                image.filename = uuid.uuid4().hex[:6].upper()
            mongo.save_file(image.filename, image)
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, {"$set": {"img": image.filename}})
        #update the rest of the fields
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_category": request.form.get("recipe_category"),
            "diet_type": request.form.getlist("diet_type"),
            "ingredients": request.form.getlist('ingredient'),
            "cooking_directions": request.form.getlist('cooking_directions'),
            "link": request.form.get("link"),
        }
            #only update the fields that are reference in "submit" dictionary, leaving image untouched
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Successfully Updated")
        return redirect(url_for('get_recipes'))
    
    #dtype gets the values of the "diet_type" array in a specific recipe and returns a list of these values(array)
    dtype = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}, { "diet_type": 1, "_id": 0 }).get("diet_type")
    categories = mongo.db.categories.find().sort("category_name", 1)
    diet_types = mongo.db.diet_types.find().sort("diet_name", 1)
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe, categories=categories, diet_types=diet_types, dtype=dtype)



#Route to delete a recipe

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


#Route to access uploaded image from gridfs

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


#Route to get diet_types

@app.route('/get_diet_types')
def get_diet_types():
    diet_types = list(mongo.db.diet_types.find().sort("diet_name", 1))
    return render_template('diet_types.html', diet_types=diet_types)


#Route to add diet types

@app.route('/add_diet_type', methods=["GET", "POST"])
def add_diet_type():
    if request.method == "POST":
        diet_type = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diet_types.insert_one(diet_type)
        flash("New Diet Type Added")
        return redirect(url_for("get_diet_types"))
    return render_template('add_diet_type.html')


#Route to delete diet type

@app.route('/delete_diet_type/<diet_id>')
def delete_diet_type(diet_id):
    mongo.db.diet_types.remove({"_id": ObjectId(diet_id)})
    flash("Diet Successfully Deleted")
    return redirect(url_for('get_diet_types'))


#Route to edit diet type

@app.route('/edit_diet_type/<diet_id>', methods=["GET", "POST"])
def edit_diet_type(diet_id):
    if request.method == "POST":
        submit = {
            "diet_name": request.form.get("diet_name")
        }
        mongo.db.diet_types.update({"_id": ObjectId(diet_id)}, submit)
        flash("Diet Successfully Updated")
        return redirect(url_for("get_diet_types"))

    diet_type = mongo.db.diet_types.find_one({"_id": ObjectId(diet_id)})
    return render_template('edit_diet_type.html', diet_type=diet_type)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)