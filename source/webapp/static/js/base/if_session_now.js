$(function () {
    if (document.cookie.includes("session_number") === true) {
        function get_cookie(cookie_name) {
            let results = document.cookie.match('(^|;) ?' + cookie_name + '=([^;]*)(;|$)');
            if (results)
                return (unescape(results[2]));
        }

        $("#session_number").attr('href', "/session/" + get_cookie("session_number") + "/result")
            .text('Сессия не закрыта').addClass("bg-danger p-2");
    } else {
        $("#session_number").hide();
    }
});