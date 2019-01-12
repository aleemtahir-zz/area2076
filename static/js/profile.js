$(document).ready(function() {

	//Navbar Selection
	$('#nav > a').each(function(){

		$(this).on('click', function(){
			var navId = this.id;
			var blockId = navId.split('-')[0];	
			console.log(blockId+'   show');
			$('#report').hide();
			$('#team').hide();
			
			$('#'+blockId).show();

		});

	});


	$.get('/api/users/?role=SM').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="smanager col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="140px" height="140px">'+
							  '<h4>'+v.name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#smanager").append(element);			  
		});
	});

	$.get('/api/users/?role=SO').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="sofficer col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="140px" height="140px">'+
							  '<h4>'+v.name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#sofficer").append(element);			  
		});
	});

	$.get('/api/users/?role=SR').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="srepresentative col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="140px" height="140px">'+
							  '<h4>'+v.name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#srepresentative").append(element);			  
		});
	});


});