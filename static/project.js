"use strict";

// USER LOGIN

const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// getting elements we need to work with and setting them as variables

// adding an event listener for login button click
loginButton.addEventListener("click", (evt) => {
    evt.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
// setting username and password as variables with values 
// from login form

// setting a dummy password and username for now
// will need to place to store new user's pw/username/email
// for future logins

    if (username === "user" && password === "12345") {
        alert("You have successfully logged in.");
        location.load("/input-form.html");      // need to change to load input-form.html
    } else {
        loginErrorMsg.style.opacity = 1;        
        // error msg is set to show with opacity of 1
    }
})


// INPUT NEW ENTRY

function inputEntry(evt) {
    evt.preventDefault();
    
    const formData = {"entry-form": $("#entry-field").val(),
                "qty": $("#entry-field").val()}
    $.post('/input-form', formData, (data) => {

$("#input-form").on('submit', inputEntry);

})

// SHOW GROWLOG

function showGrowlog(evt) {
    evt.preventDefault();
    $.get('/growlogs', (data) => {
        $('#growlog-entries').html(data) 
    
    // TODO: get the user's growlogs and show it in the div

$('#get-entries-button').on('click', showGrowlog);
  
  
// looking for button id (#) 
// .on('') = event listener
})