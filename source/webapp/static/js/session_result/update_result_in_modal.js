$(function () {
    for (let i = 1; i <= $('.number').length; i++) {
        $(document.getElementsByClassName("number")[i-1]).text(i);
    }
});
$('.edit_result').on('click', function () {
    const input_1 = $(this).attr("data-done-number");
    const input_2 = $(this).attr("data-done_with_hint-number");
    const link_1 = $(this).attr("data-update-url");
    $('#done').attr('value', input_1);
    $('#done_with_hint').attr('value', input_2);
    $('#link').attr('action', link_1);
});