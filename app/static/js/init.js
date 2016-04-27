$(document).ready(function(){
	$('.range_sum').change(function(){
		var button = $(this);
		var pk = button.attr('data-pk');
		var add = $(this).parent().find(".range_sum").val()
		console.log(add)
		$.ajax({
			url: 'http://127.0.0.1:8000/suma/' + pk,
			type: 'POST',
			data: {
				add: add,
				csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
			},
			success: function(data){
				var total_general = 0
				button.parent().find('.total_value').text(data.expenses_now);
				var total = data.expenses_now;
				total_general = total + total_general
				console.log(total_general) 
			},
			error: function(){
				alert('bad job');
			}
		});
	});
});