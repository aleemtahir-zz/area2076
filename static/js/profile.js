$(document).ready(function() {

	//Navbar Selection
	$('.profile-usermenu li').each(function(){

		$(this).on('click', function(){
			var navId = this.id;
			var blockId = navId.split('-')[0];	
			
			$('.profile-usermenu ul.nav').children().each(function(){

				if($(this).hasClass('active')){
					let navId = this.id;
					let blockId = navId.split('-')[0];
					$('#'+blockId).hide();
				}
				$(this).removeClass('active');
			});

			$(this).addClass('active');
			$('#'+blockId).show();
			console.log(blockId+'   show');

		});

	});


	$.get('/api/users/?role=SM').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="smanager col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="150px" height="150px">'+
							  '<h4>'+v.first_name+' '+v.last_name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#smanager").append(element);			  
		});
	});

	$.get('/api/users/?role=SO').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="sofficer col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="150px" height="150px">'+
							  '<h4>'+v.first_name+' '+v.last_name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#sofficer").append(element);			  
		});
	});

	$.get('/api/users/?role=SR').done(function(data){
	    $.each(data.results, function(k, v) {
		    let element = '<div class="srepresentative col-lg-3 col-sm-6 text-center mb-3">'+
							  '<img class="rounded-circle img-fluid d-block mx-auto" src="'+v.avatar.replace('/api/users','')+'" alt="" width="150px" height="150px">'+
							  '<h4>'+v.first_name+' '+v.last_name+
							    '<small>'+v.code+'</small>'+
							  '</h4>'+
						  '</div>';
			$("#srepresentative").append(element);			  
		});
	});


});