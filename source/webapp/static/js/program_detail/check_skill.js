$(function () {
    (!$("#001").text()) ? $("#01").text('Нет закрытых навыков') && $("#table_1").hide() : null;
    (!$("#002").text()) ? $("#02").text('Нет открытых навыков') && $("#table_2").hide() : null;
    (!$("#003").text()) ? $("#03").text('Сессии не проводились') : null;
});