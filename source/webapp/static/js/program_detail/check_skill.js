(() => {
    (!$("#is_there_skills").text()) ? $("#no_session").text('Нет навыков в программе') && $("#table_1").hide() : null;
    (!$("#is_there_close_skill").text()) ? $("#close_skill").text('Нет закрытых навыков') && $("#table_2").hide() : null;
    (!$("#is_there_open_skill").text()) ? $("#open_skill").text('Нет открытых навыков') && $("#table_3").hide() : null;
    (!$("#is_there_session").text()) ? $("#session").text('Сессии не проводились') : null;
})();