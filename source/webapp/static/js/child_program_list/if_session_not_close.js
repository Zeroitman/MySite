$('.btn-success').on('click', function () {
    (document.cookie.includes("session_number") === false) ?
        $('.btn-success').attr('href', "/program/" + $(this).attr("number") + "/session") :
        alert("Предыдущая сессия не закрыта!");
});