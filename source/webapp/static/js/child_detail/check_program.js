$(function () {
    (!$(document.getElementById("001")).text()) ? $(document.getElementById("01")).text('Нет открытых программм') :
        null;
    (!$(document.getElementById("002")).text()) ? $(document.getElementById("02")).text('Нет закрытых  программ') :
        null;
});