function updateStatus(date, goal_id, status, cell_id) {
    $.post("/goals/update_status/", { date: date, goal_id: goal_id, status: status })
    .done(function(data) {
        if (status) {
	        $('#'+cell_id).css('background', 'green').html('Yes').addClass('goal_cell');
        } else {
	        $('#'+cell_id).css('background', 'red').html('No').addClass('goal_cell');
        }
    });
}

function deleteGoal(goal_id) {
    $.post("/goals/delete_goal/", { goal_id: goal_id });
    $('.goal_' + goal_id).remove();
}

$(document).ready(function(){
    $('.update_goal').click(function(){
	    $.post("/goals/update_status/", { input: $('#input').val() })
	    .done(function(data) {
		    $('#output').val(data.output);
	    });
    });
    $('#save_goal').click(function(){
	    $.post("/goals/save_goal/", { statement: $('#goal_statement').val() })
    });
	$("#paragraph").keyup(function(event) {
 	$.get("/profiles/replace_words_api/", { paragraph: $('#paragraph').val() })
	.done(function(data) {
		$('#new_paragraph').html(data.paragraph);
	});
	});
});
