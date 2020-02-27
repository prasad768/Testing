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
//When Edit button is clicked, store the event Id in to "IdNo" hidden field


/*
			data : {
				newsdate : $('#newsdate').date(),
				header : $('header').val()
				type : $('type').val()
				impact : $('impact').int()
				impactrationale : $('impactrationale').val()
				url : $('url').url()
				effectivedate : $('effective').date()
				
			}*/
			
			
	/*			$.ajax({
			data : {
				test: 'Hello'
			},
			type : 'Get',
			url : '/test'
		}) */