$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.modal').modal();
    $('select').formSelect();
    dietTypeColor();
    validateMaterializeSelect();
    $('.validate-input').submit(function() {
        //prevent empty inputs from being submitted into arrays
        $(this).find(':input').filter(function() { 
            return !this.value; 
        }).attr('disabled', 'disabled');
        return true; 
    });
});


// Add dynamic ingredient input fields
let ingredientCounter = 3;
let ingredientLimit = 20;
function addInput(divId){
     if (ingredientCounter == ingredientLimit)  {
          alert("You have reached the limit of adding " + ingredientCounter + " ingredients");
     }
     else {
          var newInputDiv = document.createElement('div');
          newInputDiv.classList.add("input-field");
          newInputDiv.innerHTML = "<label for='ingredient'>Ingedient " + (ingredientCounter + 1)+ "</label>" + " <input id='ingredient' name='ingredient' type='text' />";
          document.getElementById(divId).appendChild(newInputDiv);
          ingredientCounter++;
     }
}

// Add dynamic cooking instructions input fields
let cookingCounter = 3;
let cookingLimit = 20;
function addCookingInput(divId){
     if (cookingCounter == cookingLimit)  {
          alert("You have reached the limit of adding " + cookingCounter + " paragraphs");
     }
     else {
          var newInputDiv = document.createElement('div');
          newInputDiv.classList.add("input-field");
          newInputDiv.innerHTML = "<label for='cooking_directions'>Step " + (cookingCounter + 1)+ "</label>" + " <input id='cooking_directions' name='cooking_directions' type='text' />";
          document.getElementById(divId).appendChild(newInputDiv);
          cookingCounter++;
     }
}

// The following code was taken from the CodeInstitute course material and adapte to my project:

        function validateMaterializeSelect() {
            let classValid = {"border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50"};
            let classInvalid = {"border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336"};
            if ($('select.validate').prop("required")) {
                $('select.validate').css({"dispay": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute"});
            }
            $('.select-wrapper input.select-dropdown').on("focusin", function() {
                $(this).parent(".select-wrapper").on("change", function() {
                    if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function() { })) {
                        $(this).children("input").css(classValid);
                    }
                });
            }).on("click", function() {
                if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css('background-color') === "rgba(0,0,0,0.03)") {
                    $(this).parent(".select-wrapper").children("input").css(classValid);
                } else {
                    $(".select-wrapper input.select-dropdown").on("focusout", function() {
                        if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                            if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                                $(this).parent(".select-wrapper").children("input").css(classInvalid);
                            }
                        }
                    });
                }
            });
        }
 // End code

//Function to color code diet types
 function dietTypeColor() {
    var type = $('.diet-type');
    var i;
    for (i = 0; i < type.length; i++) {
        if ((type[i].innerHTML) == "Pescatarian") {
            type[i].classList.add('blue-text');
        } else if ((type[i].innerHTML) == "Gluten-free") {
            type[i].classList.add('orange-text');
        } else if ((type[i].innerHTML) == "Raw") {
            type[i].classList.add('pink-text');
        } else if ((type[i].innerHTML) == "Vegetarian") {
            type[i].classList.add('teal-text');
        } else if ((type[i].innerHTML) == "Vegan"){
            type[i].classList.add('green-text');
        } else {
            type[i].classList.add('black-text');
        }
    }
}; 

