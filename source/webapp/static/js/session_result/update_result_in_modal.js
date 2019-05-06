$(function () {
    for (let i = 1; i <= document.getElementsByClassName("number").length; i++) {
        $(document.getElementsByClassName("number")[i - 1]).text(i);
    }
});

function getEl(id) {
    let modal = document.getElementsByName('data');
    const new_id = Number.parseInt(id);
    for (let i = 0; i < modal.length; i++) {
        let pk_result = (modal[i].attributes[7].value);
        const new_pk_result = Number.parseInt(pk_result);
        if (new_pk_result === new_id) {
            let input_1 = modal[i].attributes[8].value;
            let input_2 = modal[i].attributes[9].value;
            $(document.getElementsByName('done')).attr('value', input_1);
            $(document.getElementsByName('done_with_hint')).attr('value', input_2);
            let link_1 = (modal[i].attributes[6].value);
            $(document.getElementsByName('link')).attr('action', link_1);
            break
        }
    }
}