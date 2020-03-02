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


function saveEvent () {
alert('Save is called');
		$.ajax({
			data : {
				header : header
				impactrationale : impactrationale
			},
			type : 'Post',
			url : '/saveEvent'
		})
		.done(function(data) {
		$("[id*=Save]").bind("click", function () {
            var user = {};
            user.header = $("[id*=header]").val();
            user.impactrationale = $("[id*=impactrationale]").val();
            user.url = $("[id*=url]").val();
            });
}            
            