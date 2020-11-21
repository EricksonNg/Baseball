var updateselectionfield3 = function(){

    var user_selection_field = document.getElementById("team");
    var languages = document.getElementById("player");

    //you can use crtl-shift-i to see what this prints out, but essentially its just the html objects
    console.log("This is the user selection form:", user_selection_field);
    console.log("THis is the languages selection form:", languages);

    user_selection_field.onchange = function(){

    var name = user_selection_field.value; //grabs the data selected by the user and save in variable
    console.log("The current selected user:", name)

    fetch('/getdata3/'+ name)
      .then(response => response.json()) //converted fetched data into json

      .then(function(data){ // when fetch is done
        console.log("fetched data:",data);// use crtl-shift-i to look at data

        var options = languages.getElementsByTagName("option");
        console.log(options);// use crtl-shift-i to look at data

        for(i=0; i<data.data.length; i++){ // change all the options on select field to data we got from fetch
          options[i].text = data.data[i][1]; //parse fetched data and rewrite the selection form
          options[i].value = data.data[i][0]; //update the value of options within the selection form
        }

      });




  }



}

//calling the function
updateselectionfield3();