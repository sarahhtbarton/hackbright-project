$("input[type='radio']:checked").val();
"blacklisted"
$("input[type='radio']:checked").val();
"whitelisted"
$("input[type='radio']").is(":checked")
true
$('input[type=radio]').is(":checked")
true



$("#get-letters").on("submit", (evt) => {
    evt.preventDefault();
    console.log("working");
    if ($("input[type='radio']").is(":checked") === false) {
        evt.preventDefault();
        alert("You must select a radio button");
    } else {
        alert("We submitted your feedback");
    }
});

$("#get-letters").on("submit", (evt) => {
    evt.preventDefault();
    console.log("working");
    alert("An Alert Instead!");
});





for word ...
  append word to div in html