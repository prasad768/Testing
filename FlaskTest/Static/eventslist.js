function getEvent(idval) {
		$.ajax({
			data : {
				id : idval
			},
			type : 'Get',
			url : '/getevent'
		})
		.done(function(data) {
    		$("input[name=header]").val(data['header']);
			//alert(data);
		});
}

function saveEvent (header) {
alert('Save is called');
		$.ajax({
			data : {
				header: header
			},
			type : 'Post',
			url : '/saveevent'
		})
		.done(function(data) {
    		$("input[name=header]").val(data['header']);
			//alert(data);
		});

}