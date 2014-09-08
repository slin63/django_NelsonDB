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
			$('#selected_pedigree').dataTable({
				"searching": false,
				"scrollY": "300px",
  			"scrollCollapse": true,
  			"paginate": false
				});
		});
});

$('#localitysuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_locality/', {suggestion: query}, function(data){
			$('#localitys').html(data);
			$('#selected_locality').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#fieldsuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_field/', {suggestion: query}, function(data){
			$('#fields').html(data);
			$('#selected_field').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#collectionsuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_collecting/', {suggestion: query}, function(data){
			$('#collections').html(data);
			$('#selected_collection').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#sourcesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_source/', {suggestion: query}, function(data){
			$('#sources').html(data);
			$('#selected_source').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#taxonomysuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/mine/suggest_taxonomy/', {suggestion: query}, function(data){
			$('#taxonomy').html(data);
			$('#selected_taxonomy').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#legacypedigreesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				var radio;
				radio = $('input:radio[name=query_pedigree_option]:checked').val();
				$.get('/legacy/suggest_legacy_pedigree/', {suggestion: query, radio: radio}, function(data){
			$('#legacy_pedigrees').html(data);
			$('#selected_legacy_pedigree').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('input:radio[name=query_pedigree_option]').click(function(){
				var query;
				query = $('#legacypedigreesuggestion').val();
				var radio;
				radio = $(this).val();
				$.get('/legacy/suggest_legacy_pedigree/', {suggestion: query, radio: radio}, function(data){
			$('#legacy_pedigrees').html(data);
			$('#selected_legacy_pedigree').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#legacyexperimentsuggestion').keyup(function(){
				var query;
				query = $(this).val();
				var radio;
				radio = $('input:radio[name=query_experiment_option]:checked').val();
				$.get('/legacy/suggest_legacy_experiment/', {suggestion: query, radio: radio}, function(data){
			$('#legacy_experiments').html(data);
			$('#selected_legacy_experiment').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('input:radio[name=query_experiment_option]').click(function(){
				var query;
				query = $('#legacyexperimentsuggestion').val();
				var radio;
				radio = $(this).val();
				$.get('/legacy/suggest_legacy_experiment/', {suggestion: query, radio: radio}, function(data){
			$('#legacy_experiments').html(data);
			$('#selected_legacy_experiment').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$(document).ready(function() {
		$('#selected_stocks').dataTable();
} );

$(document).ready(function() {
		$('#selected_legacy_stock_child_row').dataTable({
			"searching": false,
			"scrollY": "500px",
			"scrollCollapse": true,
			"paginate": false
			});
} );
