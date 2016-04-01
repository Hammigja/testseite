jQuery(window).load(function () {
    document.getElementById("new_line").focus();

    jQuery('button.delete').click(delete_item);
    jQuery('button.add').click(add_item);
    jQuery('input#new_line').keypress(trigger_button_on_enter);
    jQuery('button.delete_all').click(delete_all);

});


trigger_button_on_enter = function (e) {
    var key = e.which;
    if (key == 13)  // the enter key code
    {
        $('button.add').click();
        return false;
    }
};

add_item = function (e) {
    item = jQuery('input#new_line');
    add = item.val();

    console.log(add);

    jQuery.post('./add_item', {'new_line': add}, function (htm) {
        console.log('item was add!');
        console.log(htm);
        window.location.reload();
    })
};


delete_item = function (e) {
    item = jQuery(e.currentTarget);
    nummer = item.attr('item_number');

    console.log(nummer);

    jQuery.post('./delete_item', {'zeile': nummer}, function (htm) {
        console.log('item was deleted!');
        console.log(htm);
        window.location.reload();
    })
};

delete_all = function (e) {
    jQuery.post('./delete_all', function (htm) {
        console.log('all items were deleted!');
        console.log(htm);
        window.location.reload();
    })
};
