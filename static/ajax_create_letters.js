
$('#get-letters').on('submit', (evt) => {
    evt.preventDefault();

    const formData = {
        "all-letters": $('[name="all-letters"]').val(),
        "required-letter": $('[name="required-letter"]').val()
    };

    // make a post request -- POSTING something to database. Get = Read, Post = write
    $.post('/ajax-create-letters', formData, (res) => {
        console.log(res.words);

        let wordsList = res.words;
        for (const word of wordsList) {
            $('#append-words-here').append(`<div>${word}</div>`);
        }

        // maybe put in a div where you can show a success/failure message
    });
});