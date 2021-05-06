// "use strict";

$('#get-letters').on('submit', (evt) => {
    evt.preventDefault();

    $('#word-columns').html(""); //clears out the old words
    $('#key').html(""); //clears out the old words

    const formData = {
        "all-letters": $('[name="all-letters"]').val(),
        "required-letter": $('[name="required-letter"]').val()
    };

    $.post('/ajax-create-letters', formData, (res) => {
        console.log(res);

        for (word in res) { // should probably make one div, and then add classes to it depending on what conditions it meets...
            if (res[word]['blacklist_count'] > 0) {
                $('#word-columns').append(`<div class="blacklisted">${word}</div>`);
            } else if (res[word]['whitelistlist_count'] > 0) {
                $('#word-columns').append(`<div class="whitelisted">${word}</div>`);
            } else if (res[word]['pentagram'] === true) {
                $('#word-columns').append(`<div><mark>${word}</mark></div>`);
            } else {
                $('#word-columns').append(`<div>${word}</div>`);
            }
        }
        $('#key').append(`<br>
                          <div><b>Key:</b></div>
                          <div><mark>Pentagram highlighted in yellow</mark></div>
                          <div><del>Blacklisted words in strikethrough</del></div>
                          <div>Whitelisted words have an asterisk*</div>`);
    });

    // $("#get-letters")[0].reset(); //clears the form

});