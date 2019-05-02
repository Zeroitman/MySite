$(function () {
    $('.btn').prop('disabled', true);
    $('.form-control').keyup(function () {
        ($('#field').val()) ? $('.btn').prop('disabled', false) : $('.btn').prop('disabled', true);
    });
});