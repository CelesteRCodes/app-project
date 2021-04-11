"use strict";


// PART 3: INPUT NEW ENTRY

function inputEntry(evt) {
    evt.preventDefault();
    
    const formData = {"entry-form": $("#entry-field").val(),
                "qty": $("#entry-field").val()}
    $.post('/input-form', formData, (data) => {
       
        
    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)


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