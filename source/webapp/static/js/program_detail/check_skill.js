$(function () {
    (!$(document.getElementById("001")).text()) ? $(document.getElementById("01")).text('Нет выполненных навыков') : null;
    (!$(document.getElementById("002")).text()) ? $(document.getElementById("02")).text('Нет невыполненных навыков') : null;
});
