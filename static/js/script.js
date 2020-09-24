$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.modal').modal();
    $('select').formSelect();
    });



let ingredientCounter = 1;
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