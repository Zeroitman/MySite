function counterDone(id, event) {
    event.preventDefault();

    let elem = $('#' + id);
    let num = parseInt(elem.text()) + 1;
    elem.empty().append(num);

    let form_elem = $('#form-' + id);
    let url = form_elem.attr('action');
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: url,
        data: {
            counter: num,
            csrfmiddlewaretoken: csrftoken

        },
        type: 'POST',
    });


}



function counterDoneWithHint(id, event) {
    event.preventDefault();
    let elem = $('#' + id);
    let num = parseInt(elem.text()) + 1;
    elem.empty().append(num);

    let form_elem = $('#form-' + id);
    let url = form_elem.attr('action');
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: url,
        data: {
            counter: num,
            csrfmiddlewaretoken: csrftoken

        },
        type: 'POST',

    });


}