// "use strict";

$('#get-letters').on('submit', (evt) => {
    evt.preventDefault();

    const formData = {
        "all-letters": $('[name="all-letters"]').val(),
        "required-letter": $('[name="required-letter"]').val()
    };

    $.post('/ajax-create-letters', formData, (res) => {
        console.log(res);

        for (word in res) { // should probably make one div, and then add classes to it depending on what conditions it meets...
            if (res[word]['blacklist_count'] > 0) {
                $('#append-words-here').append(`<div class="blacklisted">${word}</div>`);
            } else if (res[word]['whitelistlist_count'] > 0) {
                $('#append-words-here').append(`<div class="whitelisted">${word}</div>`);
            } else if (res[word]['pentagram'] === true) {
                $('#append-words-here').append(`<div class="pentagram">${word}</div>`);
            } else {
                $('#append-words-here').append(`<div>${word}</div>`);
            }
        }
    });

    $("#get-letters")[0].reset();
    
});