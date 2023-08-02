const element = $('<li>Item</li>');
$('#add_item').click(function() {
    $('UL.my_list').append(element);
});