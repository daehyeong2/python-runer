function runCode() {
	var code = $('#code').val();
	$.ajax({
		url: 'http://localhost:5000/run',
		type: 'POST',
		dataType: 'json',
		data: JSON.stringify({code: code}),
		contentType: 'application/json',
		success: function(data) {
			$('#output').html(data.output);
		},
		error: function(xhr, status, error) {
			console.error(error);
		}
	});
}
