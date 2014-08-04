$(document).ready(function() {
	$('#likes').click(function(){
		var catid;
		catid = $(this).attr("data-catid");
			$.get('/mine/like_category/', {category_id: catid}, function(data){
				$('#like_count').html(data);
				$('#likes').hide();
			});
	});
});

$('#catsuggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/mine/suggest_category/', {suggestion: query}, function(data){
			$('#cats').html(data);
        });
});

$('#expsuggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/mine/suggest_experiment/', {suggestion: query}, function(data){
			$('#exps').html(data);
        });
});

$('#pedigreesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_pedigree/', {suggestion: query}, function(data){
			$('#passports').html(data);
				});
});

$('#localitysuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_locality/', {suggestion: query}, function(data){
			$('#localitys').html(data);
				});
});

$('#fieldsuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_field/', {suggestion: query}, function(data){
			$('#fields').html(data);
				});
});

$(document).ready(function() {
		$('#selected_stocks').dataTable();
} );
