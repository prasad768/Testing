function getEvent(idval) {
		$.ajax({
			data : {
				id : idval
			},
			type : 'Get',
			url : '/getevent'
		})
		.done(function(data) {
		    $("input[name=newsdate]").val(data['newsdate']);
    		$("input[name=header]").val(data['header']);
    		$("input[name=type").val(data['type']);
    		$("input[name=impact]").val(data['impact']);
    		$("input[name=impactrationale]").val(data['impactrationale']);
    		$("input[name=url]").val(data['url']);
    		$("input[name=effectivedate]").val(data['effectivedate']);
    		

		});
}

function saveEvent (idval) {
alert('Save is called');
		$.ajax({
			data : {
				    header: $("input[id=header]").val(),
				    id:idval
		    },

			type : 'Post',
			url : '/saveEvent'
		})
		.done(function(data) {
    		$("input[id=header]").val(data['header']);

			//alert(data);
		});

}

		
