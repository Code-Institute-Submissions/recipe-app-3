# SmartMeals

Welcome to [SmartMeals](https://food-recipe-app1.herokuapp.com/) - easy way to store your favorite recipes! Create, update or delete any recipe, search them by diet type or meal course type and have your online cookbook easily accesible when you are ready to prepare your meals.


## Table of contents

1. [UX](#UX)
2. [Design](#Design)
3. [Database Structure](#Database-Structure)
4. [Features](#Features)
5. [Technologies](#Technologies)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

The website can be found [here](https://food-recipe-app1.herokuapp.com/).
 
## UX
 
The website has been designed to give all users access to a public online cookbook without a need to register or log in. All users have equal access to create, read, update or delete recipes from the website. Since, this is a public online resource, all users can also add, update or delete the diet types that are used to catgorize recipes.

### User stories:

> As somebody who likes to cook at home, I want to have a collection of my recipes handy, where I can add or update recipes when I need to, so that I can easily find and access them next time I'm planning a meal, without having to search on multiple food blogs at the same time.

> As a recently transitioned vegan, I'm having to spend a lot of time searching for meal ideas on different resources. There are recipes that I tired so far and enjoyed them, so it would be nice to have a space where I can save all them in full, including the source where I found them, so I can easily access them later when I want to prepare them again.

> As a mom of a family where some family members have diet restrictions, I want to have a cookbook where I can save recipes marking them with diet types and search them by diet preference when I need a specific one, preview the ingredients, so I can decide on a meal for dinner faster based on the type and ingredients.

### WireFrames

The following WireFrames were used for this project:
- [Main Page - Desktop version](https://github.com/aavasylenko/recipe-app/blob/master/Page_1.png)
- [Main Page - iPhone X version](https://github.com/aavasylenko/recipe-app/blob/master/Page_2.png)
- [Main Page - iPad version](https://github.com/aavasylenko/recipe-app/blob/master/Page_3.png)

### Design
---
#### Color Scheme
The design of the website has minimalistic approach and is inspired by [CodeInstitute](https://courses.codeinstitute.net/program/FullstackWebDeveloper) instructional videos. The color palette used is called "Deep Purple" on Materialize.css and can be found [here](https://materializecss.com/color.html).  

#### Fonts
The font family used across entire website is [Ubuntu](https://fonts.google.com/specimen/Ubuntu?query=ubun).

#### Icons
All the icons are taken from [Font Awesome](https://fontawesome.com/icons?d=gallery&m=free).

### Database Structure
---
The database for this website consists of three main MongoDB collections and two GridFS collections for storing media.
#### 1. Recipies:
- _id: ObjectId
- recipe_name: string
- recipe_category: string
- diet_type: array
- ingredients: array
- cooking_instructions: array
- link: string
- img: file

#### 2. Categories:
- _id: ObjectId
- category_name: string

#### 3. Diet Types
- _id: ObjectId
- diet_name: string

Both GridFS collections are ```fs.files``` and ```fs.chunks```. Content of these databases is automatically generated when the image is uploaded to the database. It then binds the file name from ***Recipes*** collection to the binary data stored in the above two collections.

#### Relations
- ```diet_name``` from ```diet_types``` collection is related to ```diet_type``` array in ```recipes``` collection. Multiple diet types can be chosen from ```diet_types``` collection and stored in the referenced array.
- ```category_name``` in ```categories``` is related to ```recipe_category``` in ```recipes``` collection and should only be chosen from the existing list in ```categories``` collection.
- ```img``` is referenced by two GridFs collections ```fs.files``` and ```fs.chunks``` thats binded his way:
```recipes.img -> fs.files[filename] -> fs.chunks[files_id]```.

## Features
 
### Existing Features
#### Homepage
- Users can browse recipes and view all of them on the main page. Search bar allows users to search the entire database of recipes and will search for keywords in recipes names, ingredients, cooking instructions and it will also search by diet types.
- On cliking on a recipe card user will see the list of ingredients required without being rerouted anywhere.
- In addition, by cicking on the card user will se ptions to edit or delete the recipe. By clicking on "delete" button user will be asked a confirmation to prevent unintentional removal.
- Top navigation bar provides an option to view recipes by meal course if a user wishes to only see meals for a specific course.

#### Recipe
- Once the user clicks on the recipe card, he will be able to preview the list of ingredients. However to see the cooking instructions, he will have to click on "Directions" and a modal with cooking directions will pop up. If the recipe has a source link - the user will see it in this modal as well.

#### Add a new recipe
- From the top navigation bar, user can click on "New Recipe" and he will be rerouted to fill out a form to add a new recipe. The form is user-friendly an intuitive and has some custom validation to indicate whic fields are required. Once the user clicks on a required field and leaves it empty - the field will turn red.
- User can choose multiple values in **Diet Type** field. The values are populated from ```diet_types``` collections and they will be submitted into ```diet_type``` array in ```recipes``` collection.
- Both **Ingredients** and **Cooking Directions** fields have ```array``` type in the database. User is asked to put each new ingredient or cooking instructions step on a new line. Each field has a ```+``` button to add new rows if the user needs to add more than three rows into each field. The rows are then stored in the database, each as a separate item of a respective array. The counter for each new input starts based on the number of the last input. This is achieved through JavaScript functions. If user created more inputs in these fileds than he filled out - the empty inputs will not be submitted into the database.
- **Picture** and **Source Link** fields are optional. If user chooses not to submit an image, then the default "No image available" picture will show up in the recipe card. Alternatevily, if the user leaves **Source Link** filed empty - no link or text for it will show up in the recipe modal.


#### Edit Recipe
- User can edit a recipe by clicking on "Edit" button inside the recipe card.
- The form will be pre-populated with the values from the database for a specific recipe.
- The same rules apply to optional fields, but since image field is impossible to pre-populate, it shows up in this form as an empty file input. However on submitting the form, the image field will not be updated to an empty string if the user did not upload a new image. This is done to allow the user to update the image if needed, or leave it untouched if the user only wants to update the recipe but leave the same image.
- Empty input fields will not be submitted into the database.

#### Manage Diet Types
- Users are allowed to to create, update or delete the existing diet types. 
- Buttons are user-friendly and intuitive, and for diet types user only needs the name of a particular diet.
- Confirmation modal will pop up before deleting a diet type.
- All the existing diet types are color coded, but any new ones will default to black text color.


### Features Left to Implement
- In the future I'd like to implement rating scale for each recipe and ***Sort by rating*** option.

## Technologies Used

### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,scripting%20languages%20such%20as%20JavaScript.)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

### Libraries and frameworks:
- [JQuery](https://jquery.com)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Materialize.css](https://materializecss.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

### Database
- [MongoDB](https://www.mongodb.com/)

### Deployment
- [Heroku](https://www.heroku.com/)


## Testing
All tests are preformed in Google Chrome, Mozilla Firefox, and Microsoft Edge on Desktop, and native Android browser.

### Responsiveness
The website was tested to all default device sizes provided by Chrome Developer Tools:

  - 360 x 640 Galaxy S5
  - 375 x 667 iPhone 6/7/8
  - 375 x 812 iPhone X
  - 411 x 731 Pixel 2
  - 411 x 823 Pixel 2 XL
  - 414 x 736 iPhone 6/7/8 Plus
  - 768 x 1024 iPad
  - 1024 x 1366 iPad Pro
  
### Code Validators
The following validators were used to test the code quality:
- [WC3 Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffood-recipe-app1.herokuapp.com%2F) - the only errors returned are the "duplicate ID" errors. Those, however, are expected because of the input fields that are going to send data into arrays. 

- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) - no errors were returned for my ```style.css``` file.

### Manual Testing

- Try submitting an empty search string into a search bar and recieve an error that this field is required.
- Click on any recipe and open "Directions", you will see a "Source Link" with a valid URL in each one of them. Alternatevily, open the recipe called ****Vegan candy “Belochka”**** and you will not see a paragraph with the source link, becuase the link for this recipe is an empty string in the database.
- Click on "Course" in the top navbar and open each of the menu sections to verify that the right recipes are returned under each category along with the related title of the page.
- Click on "Delete" under any recipe and verify that confirmation modal pops up before the recipe is deleted.
- Click on "New Recipe" and try submitting an empty form. It will not be submitted.
- Add information to "New Recipe" form and leave some input fields under "Ingredients" or "Cooking Directions" headers empty. Then verify on the homepage, that those empty fileds were not submitted into arrays.
- Add a new recipe without providing an photo and/or source link. Verify that the recipe submitted appears on the homepage with the default "No image available" picture. Open the directions modal for the recipe and verify that the paragraph "Source Link" is absent.
- When adding a new recipe, choose more than one diet type and verify on the homepage that the diet types you chose appear correctly under the recipe.
- Click on "Edit" under a chose recipe and try submitting a form for update without a adding photo. Verify that the changes are displayed correctly and the old photo is still there. Alternatevily, click on "Edit" for an existing recipe and try submitting a form for update and add a new image. Verify that it's displayed correctly.
- Click on "Edit" under any exsiting recipe and click on the "+" button under "Ingredients" and "Cooking Direction". Verify that the label for each new input has a correct number regardless of how many input fields are already on the screen. The same text can be performed on "New Recipe" page.
- On "New Recipe" page click on any of the required fields but do not type anything. Leave them epmty. Verify that the fields are underlined with red color indicating that they are required.
- Try manipulating exsiting diet types by changing their names or deleting them. Verify that the changes are reflected correctly.

### User Stories Testing
  
> As somebody who likes to cook at home, I want to have a collection of my recipes handy, where I can add or update recipes when I need to, so that I can easily find and access them next time I'm planning a meal, without having to search on multiple food blogs at the same time.

This user was able to achieve his goal by adding his own recipes into the database, saving them and being able to easily find them using the search bar and the keywords.

> As a recently transitioned vegan, I'm having to spend a lot of time searching for meal ideas on different resources. There are recipes that I tired so far and enjoyed them, so it would be nice to have a space where I can save all them in full, including the source where I found them, so I can easily access them later when I want to prepare them again.

This user was able to achieve his goal by saving his favorite recipes into the website's database and easily finding them next time he needs the recipe. He is also able to follow the source link if he chooses to.

> As a mom of a family where some family members have diet restrictions, I want to have a cookbook where I can save recipes marking them with diet types and search them by diet preference when I need a specific one, preview the ingredients, so I can decide on a meal for dinner faster based on the type and ingredients.

This user was able to achieve her goal by using the website, searching the recipes based on diet types, easily previewing what ingredients a meal requires and making a decision whether this meal is suitable for dinner.

#### Known Issues
When adding a new recipe, using "Diet Type" field - the user is able to choose multiple options. However, the drop down will close immediately after the user made one selection. It will save the selection, but if the user needs to add more options - he will have to click on the drop down again and add another selection.



## Deployment

### Tools required to be installed
- Python 3 
- Git
- Heroku CLI

### Cloning and setting up locally instructions:
#### 1. Clone website
1. Go to [GitHub](https://github.com/aavasylenko)
2. Click Repositories.
3. Locate recipe-app.
4. Open [SmartMeals](https://github.com/aavasylenko/recipe-app)
5. Click "Download".
6. Or clone directly from the terminal using: ```got clone https://github.com/aavasylenko/recipe-app.git```

#### 2. Install Requirements.
1. Install the libraries/dependencies from requirements.txt by typing ```pip3 install -r requirements.txt``` in the terminal command field.

#### 3. Set up the database keys
1. Create a python file called ```env.py``` on the same folder level as the ```app.py```.
2. Inside the env.py file add the following code:
 on the top line ```import os```.
 Then below add these lines:

```os.environ.setdefault("IP", "0.0.0.0")```

```os.environ.setdefault("PORT", "5000")```

```os.environ.setdefault("SECRET_KEY", "<your_secret_key>")```

```os.environ.setdefault("MONGO_URI", "mongodb+srv://myRoot:_MONGODB-PASSWORD_@_CLUSTER-NAME_-96wib.mongodb.net/_DATABASE-NAME_?retryWrites=true&w=majority")```

```os.environ.setdefault("MONGO_DBNAME", "your_db_name")```


#### 4. Connection string explained
```mongodb+srv://myRoot:_MONGODB-PASSWORD_@_CLUSTER-NAME_-96wib.mongodb.net/_DATABASE-NAME_?retryWrites=true&w=majority```
1. _MONGODB-PASSWORD_ - this is your password for your MongoDB atlas account.
2. _CLUSTER-NAME_ - the name you create when setting up MongoDB for the first time. Cluster is like your project that can host multiple databases.
3. _DATABASE-NAME_ - the name of your database that hosts your collections.


#### 5. Run the Project locally
 - Run app.py


#### 6. Before commiting and pushing your code to GitHub:
- Make sure to create ```.gitignore``` file.
- Type ```env.py``` inside your ```.gitignore``` file. This is done to prevent publishing your passwords or secret keys to a public website.


### Deploy on Heroku
#### 1. Set up Heroku
1. Create an account on [Heroku](https://dashboard.heroku.com/login).
2. Click "Create new app".
3. Give it a unique name and choose your region.
4. Find your App name on the dash board.
6. Click Settings, then Config Vars, and fill in the variables from your ```env.py``` file


| Key        | Value           | 
|:------------- |:-------------| 
|  IP  | 0.0.0.0 | 
|  PORT  | 5000 | 
|  MONGO_URI  | mongodb+srv://myRoot:_MONGODB-PASSWORD_@_CLUSTER-NAME_-96wib.mongodb.net/_DATABASE-NAME_?retryWrites=true&w=majority | 
|  MONGO_DBNAME  | _DATABASE-NAME_ |
|  SECRET_KEY  | "your_secret_key" |


#### Prepare your code:
1. In your IDE create a ```Procfile```. It does not have extension and make sure you capitalize the first letter ```P```. You can do this with the following command: ```echo web: python3 app.py > Procfile```
2. Perform the following command in your terminal: ```pip3 freeze > requirements.txt```


#### 3. Deploy to Heroku
1. In your Terminal type ```heroku login -i```.
2. Log into your heroku account using your credentials.
3. Add your files to staging by running ```git add -A```
4. Commit your code: ```git commit -m "your_message_here"
5. Set up your heroku remote by running ```heroku git:remote -a <the_app_name_you_created>```
6. Then ```git push heroku master```.  
7. Start running your app using this command in your terminal ```heroku ps:scale web=1```
8. Open Heroku website.
9. Navigate to your app, and click Open App.

#### Alternative method to push to Heroku directly from GitHub
1. Push all your code to a GitHub repository.
2. On Heroku website under "Deploy" tab navigate to "App connected to GitHub"
3. Connect your GitHub account and find your GitHub repository name.
4. You can set Automatic Deploys from your chosen branch or navigate to "Manual Deploy" and click on "Deploy Branch"
5. Wait until the app is deployed and click "Open App". 

## Credits

This code was fully inspired by CodeInstitute's MongoDB project. The project has inspired me to create even more useful functionality that I would want to use myself.

### Content
- Recipes are copied from [LikeLida foodblog](https://likelida.com/)

### Media
- The photos used in this site were obtained from [LikeLida foodblog](https://likelida.com/) as well.

### Acknowledgements

- I received inspiration for this project from CodeInstitute.
