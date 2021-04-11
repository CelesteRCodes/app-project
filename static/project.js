"use strict";

// USER LOGIN

const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (evt) => {
    evt.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "12345") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
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
}