
$('#get-letters').on('submit', (evt) => {
    evt.preventDefault();
    alert("We've received your submission of today's letters. It takes about 2 minutes to for the solutions to show up, so take a little stretch break and check back soon.");

    const formData = {
        "all-letters": $('[name="all-letters"]').val(),
        "required-letter": $('[name="required-letter"]').val()
    };

    // make a post request -- POSTING something to database. Get = Read, Post = write
    $.post('/ajax-create-letters', formData, (res) => {
        console.log(res.words);

        let wordsList = res.words;
        // add a header? Like <h1>TODAYS ANSWERS</h1?
        for (const word of wordsList) {
            $('#append-words-here').append(`<div>${word}</div>`);
        }
    });
});