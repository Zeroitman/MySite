function dataGet(elementId) {
    let holdCounter = null;
    // variable with url from form data attribute
    let resultUrl = $('#form-' + elementId).attr('data-get-url');

    $.ajax({
        async: false,
        url: resultUrl,
        type: 'GET',
        success: (counter) => {
            console.log(counter);
            holdCounter = counter;
        },
        error: (error) => {
            console.log(error);
        }
    });
    return holdCounter;
}


function counterDone(id, event) {
    event.preventDefault();
    let elem = $('#' + id);
    let form_elem = $('#form-' + id);
    let counter = dataGet(id);

    let counter_done = counter['result_done'] + 1;
    let done_w_hint = counter['result_w_hint'];


    let url = form_elem.attr('action');
    elem.empty().append(counter_done + done_w_hint);
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({

        url: url,
        data: {
            counter: counter_done,
            csrfmiddlewaretoken: csrftoken

        },
        type: 'POST',

    });


}


function counterDoneWithHint(id, event) {
    event.preventDefault();
    let elem = $('#' + id);
    let form_elem = $('#form-hint-' + id);

    let counter = dataGet(id);
    let counter_w_hint = counter['result_w_hint'] + 1;
    let counter_done = counter['result_done'];


    let url = form_elem.attr('action');
    elem.empty().append(counter_done + counter_w_hint);

    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: url,
        data: {
            counter: counter_w_hint,
            csrfmiddlewaretoken: csrftoken

        },
        type: 'POST',

    });

}