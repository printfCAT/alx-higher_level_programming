const element = $('header');
$('#toggle_header').click(function() {
	if (element.hasClass('red')) {
		element.removeClass('red');
	    element.addClass('green');
	} else {
		element.removeClass('green');
		element.addClass('red');
	}
});