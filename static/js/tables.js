$(document).ready(function() {
        // $('#example').dataTable();
    var editTaskID;    
    var deleteTaskID;    
	var base_name = 'http://localhost:8000';
	$('[data-toggle="tooltip"]').tooltip();

	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});

	// Identify Task ID for edit or delete
	$(".editRecordModalBtn").each(function(){ 
		$(this).on('click', function(){
			editTaskID = $("#"+this.id).attr("task-id");
	    	// console.log(editTaskID);
			var client_name = $("#task"+editTaskID+' .client_name').text();
			var client_number = $("#task"+editTaskID+' .client_number').text();
			var client_dob = $("#task"+editTaskID+' .client_dob').text();
			var client_status = $("#task"+editTaskID+' .client_status').text();
			
			$('#editRecordModal .client_name').val(client_name);
			$('#editRecordModal .client_number').val(client_number);
			$('#editRecordModal .client_dob').val(client_dob);
			$('#editRecordModal .client_status').val(client_status);
		});
	});
	$(".deleteRecordModalBtn").each(function(){ 
		$(this).on('click', function(){
			deleteTaskID = $("#"+this.id).attr("task-id");
		});
	});

	// $.get('/api/tasks/').done(function(data){
	//     console.log(data.results);
	// });


	var csrftoken = readCookie('csrftoken');
	$(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": readCookie("csrftoken")
            }
        });
    });
	$("#addRecordModalSubmit").on('click', function(){
		let client_name = $('#addRecordModal .client_name').val();
		let client_number = $('#addRecordModal .client_number').val();
		let client_dob = $('#addRecordModal .client_dob').val();
		let client_status = $('#addRecordModal .client_status').val();

		var data = {
			'client_name': client_name, 
			'client_number': client_number, 
			'client_dob': client_dob, 
			'status': client_status, 
			'user': base_name+'/api/users/'+uid+'/'
		};
		
		if( client_name != '' && client_number != '' && client_dob != '' && client_status != '' ){

			$.post('/api/tasks/', data).done(function(data){
					// console.log(data);
			},
			{headers: {"X-CSRFToken":csrftoken }});
		}

	});

	$("#editRecordModalSubmit").on('click', function(){
		let client_name = $('#editRecordModal .client_name').val();
		let client_number = $('#editRecordModal .client_number').val();
		let client_dob = $('#editRecordModal .client_dob').val();
		let client_status = $('#editRecordModal .client_status').val();

		var data = {
			'client_name': client_name, 
			'client_number': client_number, 
			'client_dob': client_dob, 
			'status': client_status, 
			'user': base_name+'/api/users/'+uid+'/'
		};
		// console.log(editTaskID);
		if( client_name != '' && client_number != '' && client_dob != '' && client_status != '' ){

			$.ajax({
			    type: 'PUT',
			    url: '/api/tasks/'+editTaskID+'/',
			    contentType: 'application/json',
			    data: JSON.stringify(data), // access in body
			}).done(function () {
			    // console.log('SUCCESS');
			});
		}

	});

	$("#deleteRecordModalSubmit").on('click', function(){

		console.log(deleteTaskID);
		
		$.ajax({
		    type: 'DELETE',
		    url: '/api/tasks/'+deleteTaskID+'/',
		}).done(function () {
		    // console.log('SUCCESS');
		});
	});

} );

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}