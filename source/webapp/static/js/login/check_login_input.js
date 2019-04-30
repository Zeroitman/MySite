$(function () {
    $('.btn').prop('disabled', true);
    $('.form-control').keyup(function () {
        ($('#username').val() && $('#password').val()) ?
            $('.btn').prop('disabled', false) : $('.btn').prop('disabled', true);
    });
});
