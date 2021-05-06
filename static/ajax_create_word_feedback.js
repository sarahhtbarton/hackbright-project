// "use strict";

$('#get-feedback').on('submit', (evt) => {
    evt.preventDefault();

    const formData = {
        "word-feedback": $('[name="word-feedback"]').val(),
        "feedback": $('[name="feedback"]:checked').val()
    };

    $.post('/ajax-create-feedback', formData, (res) => {
        console.log(res);
        $('.alert').show();
    });
});