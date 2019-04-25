$(function () {
    $('.btn').prop('disabled', true);
    $('.form-control').keyup(function () {
        ($('#username').val() && $('#password').val()) ?
            $('.btn').prop('disabled', false) : $('.btn').prop('disabled', true);
    });
});

$(function () {
    (!$(document.getElementById("001")).text()) ? $(document.getElementById("01")).text('Нет выполненных навыков') : null;
    (!$(document.getElementById("002")).text()) ? $(document.getElementById("02")).text('Нет невыполненных навыков') : null;
});