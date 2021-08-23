const search_input = $("#search-input")
const select_author = $("#author-select")
const search_icon = $('#search-icon')
const books_div = $('#replaceable-content')
const endpoint = '/'
const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the books_div, then:
			books_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				books_div.html(response['html_from_view'])
				// fade-in the div with new contents
				books_div.fadeTo('slow', 1)
				// stop animating search icon
				search_icon.removeClass('blink')
			})
		})
}

// when start typing in search box
search_input.on('keyup', function () {

	const request_parameters = {
		q: $(this).val(), f: select_author.val() // value of search_input and select_author
	}

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

// when author selection happened
select_author.change(function(event) {

    const request_parameters = {
		f: $(this).val(), q: search_input.val()  // value of search_input and select_author
	}

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})