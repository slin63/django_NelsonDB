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

$('#show_all_seedinv_taxonomy').click(function(){
	$.get('/lab/seed_inventory/show_all_taxonomy/', {}, function(data){
		$('#taxonomies').html(data);
		$('#selected_taxonomy').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_seedinv_pedigree').click(function(){
	$.get('/lab/seed_inventory/show_all_pedigree/', {}, function(data){
		$('#pedigrees').html(data);
		$('#selected_pedigree').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#pedigreesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/lab/seed_inventory/suggest_pedigree/', {suggestion: query}, function(data){
			$('#pedigrees').html(data);
			$('#selected_pedigree').dataTable({
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
				$.get('/lab/seed_inventory/suggest_taxonomy/', {suggestion: query}, function(data){
			$('#taxonomies').html(data);
			$('#selected_taxonomy').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#show_all_isolate_taxonomy').click(function(){
	$.get('/lab/isolate_inventory/show_all_taxonomy/', {}, function(data){
		$('#isolate_taxonomies').html(data);
		$('#selected_isolate_taxonomy').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_isolate_disease').click(function(){
	$.get('/lab/isolate_inventory/show_all_disease/', {}, function(data){
		$('#isolate_disease').html(data);
		$('#selected_isolate_disease').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#isolate_taxonomysuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/lab/isolate_inventory/suggest_isolate_taxonomy/', {suggestion: query}, function(data){
			$('#isolate_taxonomies').html(data);
			$('#selected_isolate_taxonomy').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#isolate_diseasesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				$.get('/lab/isolate_inventory/suggest_isolate_disease/', {suggestion: query}, function(data){
			$('#isolate_disease').html(data);
			$('#selected_isolate_disease').dataTable({
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false
				});
		});
});

$('#row_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/row/suggest_row_experiment/', {suggestion: query}, function(data){
		$('#row_experiment').html(data);
		$('#selected_row_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_row_experiment').click(function(){
	$.get('/lab/data/row/show_all_experiment/', {}, function(data){
		$('#row_experiment').html(data);
		$('#selected_row_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#plant_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/plant/suggest_plant_experiment/', {suggestion: query}, function(data){
		$('#plant_experiment').html(data);
		$('#selected_plant_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_plant_experiment').click(function(){
	$.get('/lab/data/plant/show_all_experiment/', {}, function(data){
		$('#plant_experiment').html(data);
		$('#selected_plant_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#measurement_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/measurement/suggest_measurement_experiment/', {suggestion: query}, function(data){
		$('#measurement_experiment').html(data);
		$('#selected_measurement_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_measurement_experiment').click(function(){
	$.get('/lab/data/measurement/show_all_experiment/', {}, function(data){
		$('#measurement_experiment').html(data);
		$('#selected_measurement_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#clear_plant_experiment').click(function(){
	$.get('/lab/data/plant/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_measurement_experiment').click(function(){
	$.get('/lab/data/measurement/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_row_experiment').click(function(){
	$.get('/lab/data/row/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#legacypedigreesuggestion').keyup(function(){
				var query;
				query = $(this).val();
				var radio;
				radio = $('input:radio[name=query_pedigree_option]:checked').val();
				$.get('/legacy/checkbox_suggest_legacy_pedigree/', {suggestion: query, radio: radio}, function(data){
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
				$.get('/legacy/checkbox_suggest_legacy_pedigree/', {suggestion: query, radio: radio}, function(data){
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
				$.get('/legacy/checkbox_suggest_legacy_experiment/', {suggestion: query, radio: radio}, function(data){
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
				$.get('/legacy/checkbox_suggest_legacy_experiment/', {suggestion: query, radio: radio}, function(data){
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
	$('.selected_stocks').dataTable();
} );

$(document).ready(function() {
		$('#selected_legacy_stock_child_row').dataTable({
			"searching": false,
			"scrollY": "500px",
			"scrollCollapse": true,
			"paginate": false
			});
} );
