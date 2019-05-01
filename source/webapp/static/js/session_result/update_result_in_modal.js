function getEl(id) {
    let modal = document.getElementsByName('data');
    let input_1 = modal[id - 1].attributes[8].nodeValue;
    let input_2 = modal[id - 1].attributes[9].nodeValue;
    let value_1 = $(document.getElementsByName('done')).attr('value', input_1);
    let value_2 = $(document.getElementsByName('done_with_hint')).attr('value', input_2);
    let link_1 = (modal[id - 1].attributes[6].value);
    let link = $(document.getElementsByName('link')).attr('action', link_1);
}