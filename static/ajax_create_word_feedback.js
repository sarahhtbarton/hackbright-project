
$('#get-feedback').on('submit', (evt) => {
    evt.preventDefault();

    const formData = {
        "word-feedback": $('[name="word-feedback"]').val(),
        "feedback": $('[name="feedback"]').val()
    };

    $.post('/ajax-create-feedback', formData, (res) => {
        console.log(res);
        alert('Thanks for your feedback!');
    });
});