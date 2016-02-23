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

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
	// test that a given url is a same-origin URL
	// url could be relative or scheme relative or absolute
	var host = document.location.host; // host + port
	var protocol = document.location.protocol;
	var sr_origin = '//' + host;
	var origin = protocol + sr_origin;
	// Allow absolute or scheme relative URLs to same origin
	return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	// or any other URL that isn't scheme relative or absolute i.e relative.
	!(/^(\/\/|http:|https:).*/.test(url));
}

$(document).ready(function(){
	if ($('#stock_measurement_plot').length > 0 ) {
		$('#stock_measurement_plot_button').click( function() {

		$.ajax({
			dataType: "json",
			url: "/lab/data/stock/measurement/plot/",
			type: "POST",
			data: {'stock_id':$('#stock_detail_id').val(), 'parameter_of_interest':$('#select_parameter_to_plot').val()},
			beforeSend: function(xhr, settings) {
				var csrftoken = getCookie('csrftoken');
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			},
			success: function(data) {
				//console.log(data.data);

				var visualization = d3plus.viz()
				.container("#stock_measurement_plot")
				.data(data.data)
				.type("box")
				.id("id")
				.x("parameter")
				.y("value")
				.ui([{
					"label": "Visualization Type",
					"method": "type",
					"value": ["scatter","box"]
				}])
				.draw()

			}
		});
	});

	}

});

$('#stock_detail_delete_button').click(function(){
	if (confirm("Are you sure you want to delete this stock? It cannot be undone.")) {
		$.ajax({
			dataType: "json",
			url: "/lab/data/stock_delete/",
			type: "POST",
			data: {'stock_id':$('#stock_detail_id').val()},
			beforeSend: function(xhr, settings) {
				var csrftoken = getCookie('csrftoken');
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			},
			success: function(data) {
				location.reload();
			}
		});
	}
});

$('#show_all_seedinv_taxonomy').click(function(){
	$('#suggested_taxonomy').css('display', 'block');
	$('#selected_taxonomy').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/seed_inventory/show_all_taxonomy/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "passport__taxonomy__species"},
		{ "mData": "passport__taxonomy__population"},
		{ "mData": "pedigree"}
		],
	});
});

$('#show_all_seedinv_pedigree').click(function(){
	$('#suggested_pedigrees').css('display', 'block');
	$('#selected_pedigree').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/seed_inventory/show_all_pedigree/",
		"deferRender": true,
		"aoColumns": [
		  { "mData": "input"},
		  { "mData": "pedigree"},
		  { "mData": "passport__taxonomy__population"}
		],
	});
});

$('#show_all_seedinv_parameters').click(function(){
	$('#suggested_seedinv_parameters').css('display', 'block');
	$('#selected_seedinv_parameters').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/seed_inventory/show_all_parameters/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "measurement_parameter__parameter"},
		{ "mData": "measurement_parameter__protocol"},
		{ "mData": "measurement_parameter__unit_of_measure"}
		],
	});
});

$('#seedinvparametersuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_seedinv_parameters').css('display', 'none'); }
	else { $('#suggested_seedinv_parameters').css('display', 'block'); }
		$('#selected_seedinv_parameters').dataTable({
			"destroy": true,
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false,
			"ajax": {
				"url": "/lab/seed_inventory/suggest_parameters/",
				"type": 'POST',
				"data": {'suggestion':query},
				beforeSend: function(xhr, settings) {
					var csrftoken = getCookie('csrftoken');
					if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
						xhr.setRequestHeader("X-CSRFToken", csrftoken);
					}
				}
			},
			"deferRender": true,
			"aoColumns": [
			{ "mData": "input"},
			{ "mData": "measurement_parameter__parameter"},
			{ "mData": "measurement_parameter__protocol"},
			{ "mData": "measurement_parameter__unit_of_measure"},
			],
	});
});

$('#select_seedinv_parameters_form_submit').click(function(){
	var parameters = [];
	$("input[name='checkbox_seedinv_parameters']:checked").each(function() {
		parameters.push($(this).val());
	});
	$.ajax({
		"url": "/lab/seed_inventory/select_parameters/",
		"type": "POST",
		"data": {'parameters': JSON.stringify(parameters)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting parameters!");
		}
	});
});

$('#pedigreesuggestion').keyup(function(){
  var query = $(this).val();
	if (query == '') { $('#suggested_pedigrees').css('display', 'none'); }
	else { $('#suggested_pedigrees').css('display', 'block'); }
	$('#selected_pedigree').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": {
			"url": "/lab/seed_inventory/suggest_pedigree/",
			"type": 'POST',
			"data": {'suggestion':query},
			beforeSend: function(xhr, settings) {
				var csrftoken = getCookie('csrftoken');
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		},
		"deferRender": true,
		"aoColumns": [
		  { "mData": "input"},
		  { "mData": "pedigree"},
	    { "mData": "passport__taxonomy__population"}
    ],
  });
});

$('#select_pedigree_form_submit').click(function(){
	var pedigrees = [];
	$("input[name='checkbox_pedigree']:checked").each(function() {
		pedigrees.push($(this).val());
	});
	$.ajax({
		"url": "/lab/seed_inventory/select_pedigree/",
		"type": "POST",
		"data": {'pedigrees': JSON.stringify(pedigrees)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting pedigree!");
		}
	});
});

$('#select_taxonomy_form_submit').click(function(){
	var taxonomy = [];
	$("input[name='checkbox_taxonomy']:checked").each(function() {
		taxonomy.push($(this).val());
	});
	$.ajax({
		"url": "/lab/seed_inventory/select_taxonomy/",
		"type": "POST",
		"data": {'taxonomy': JSON.stringify(taxonomy)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting taxonomy!");
		}
	});
});

$('#taxonomysuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_taxonomy').css('display', 'none'); }
	else { $('#suggested_taxonomy').css('display', 'block'); }
			$('#selected_taxonomy').dataTable({
				"destroy": true,
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false,
				"ajax": {
					"url": "/lab/seed_inventory/suggest_taxonomy/",
					"type": 'POST',
					"data": {'suggestion':query},
					beforeSend: function(xhr, settings) {
						var csrftoken = getCookie('csrftoken');
						if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
							xhr.setRequestHeader("X-CSRFToken", csrftoken);
						}
					}
				},
				"deferRender": true,
				"aoColumns": [
				{ "mData": "input"},
				{ "mData": "passport__taxonomy__species"},
				{ "mData": "passport__taxonomy__population"},
				{ "mData": "pedigree"}
				],
			});
});

$('#seed_inventory_clear_taxonomy').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_taxonomy/",
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error clearing selected taxonomy!");
		}
	});
});

$('#seed_inventory_clear_pedigree').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_pedigree/",
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error clearing selected pedigree!");
		}
	});
});

$('#seed_inventory_clear_parameters').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_seedinv_parameters/",
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error clearing selected parameters!");
		}
	});
});

$('#isolatestock_inventory_clear_disease').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_isolatestock_disease/",
		success: function() {
			$.ajax({
				"url": "/lab/checkbox_clear/checkbox_isolatestock_disease_names/",
				success: function() {
					location.reload(true);
				},
				error: function() {
					alert("Error clearing selected isolatestock diseases!");
				}
			});
		},
		error: function() {
			alert("Error clearing selected isolatestock diseases!");
		}
	});

});

$('#isolatestock_inventory_clear_taxonomy').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_isolatestock_taxonomy/",
		success: function() {
			$.ajax({
				"url": "/lab/checkbox_clear/checkbox_isolatestock_taxonomy_names/",
				success: function() {
					location.reload(true);
				},
				error: function() {
					alert("Error clearing selected isolatestock taxonomies!");
				}
			});
		},
		error: function() {
			alert("Error clearing selected isolatestock taxonomies!");
		}
	});
});

$('#show_all_isolatestock_taxonomy').click(function(){
	$('#suggested_isolatestock_taxonomy').css('display', 'block');
	$('#selected_isolatestock_taxonomy').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/isolatestock_inventory/show_all_taxonomy/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "disease_info__common_name"},
		{ "mData": "passport__taxonomy__genus"},
		{ "mData": "passport__taxonomy__alias"},
		{ "mData": "passport__taxonomy__race"},
		{ "mData": "passport__taxonomy__subtaxa"},
		{ "mData": "passport__taxonomy__species"},
		],
	});
});

$('#show_all_isolatestock_disease').click(function(){
	$('#suggested_isolatestock_disease').css('display', 'block');
	$('#selected_isolatestock_disease').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/isolatestock_inventory/show_all_disease/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "disease_info__common_name"},
		{ "mData": "passport__taxonomy__genus"},
		],
	});
});

$('#isolatestock_taxonomysuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_isolatestock_taxonomy').css('display', 'none'); }
		else { $('#suggested_isolatestock_taxonomy').css('display', 'block'); }
			$('#selected_isolatestock_taxonomy').dataTable({
				"destroy": true,
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false,
				"ajax": {
					"url": "/lab/isolatestock_inventory/suggest_isolatestock_taxonomy/",
					"type": 'POST',
					"data": {'suggestion':query},
					beforeSend: function(xhr, settings) {
						var csrftoken = getCookie('csrftoken');
						if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
							xhr.setRequestHeader("X-CSRFToken", csrftoken);
						}
					}
				},
				"deferRender": true,
				"aoColumns": [
				{ "mData": "input"},
				{ "mData": "disease_info__common_name"},
				{ "mData": "passport__taxonomy__genus"},
				{ "mData": "passport__taxonomy__alias"},
				{ "mData": "passport__taxonomy__race"},
				{ "mData": "passport__taxonomy__subtaxa"},
				{ "mData": "passport__taxonomy__species"},
				],
			});
		});

$('#isolatestock_diseasesuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_isolatestock_disease').css('display', 'none'); }
		else { $('#suggested_isolatestock_disease').css('display', 'block'); }
			$('#selected_isolatestock_disease').dataTable({
				"destroy": true,
				"searching": false,
				"scrollY": "300px",
				"scrollCollapse": true,
				"paginate": false,
				"ajax": {
					"url": "/lab/isolatestock_inventory/suggest_isolatestock_disease/",
					"type": 'POST',
					"data": {'suggestion':query},
					beforeSend: function(xhr, settings) {
						var csrftoken = getCookie('csrftoken');
						if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
							xhr.setRequestHeader("X-CSRFToken", csrftoken);
						}
					}
				},
				"deferRender": true,
				"aoColumns": [
				{ "mData": "input"},
				{ "mData": "disease_info__common_name"},
				{ "mData": "passport__taxonomy__genus"},
				],
			});
});

$('#select_isolatestock_disease_form_submit').click(function(){
	var d = [];
	$("input[name='checkbox_isolatestock_disease_id']:checked").each(function() {
		d.push($(this).val());
	});
	$.ajax({
		"url": "/lab/isolatestock_inventory/select_isolatestock_disease/",
		"type": "POST",
		"data": {'diseases': JSON.stringify(d)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting isolatestock disease!");
		}
	});
});

$('#select_isolatestock_taxonomy_form_submit').click(function(){
	var d = [];
	$("input[name='checkbox_isolatestock_taxonomy_id']:checked").each(function() {
		d.push($(this).val());
	});
	$.ajax({
		"url": "/lab/isolatestock_inventory/select_isolatestock_taxonomy/",
		"type": "POST",
		"data": {'taxonomies': JSON.stringify(d)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting isolatestock taxonomy!");
		}
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

$('#microbe_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/microbe/suggest_microbe_experiment/', {suggestion: query}, function(data){
		$('#microbe_experiment').html(data);
		$('#selected_microbe_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_microbe_experiment').click(function(){
	$.get('/lab/data/microbe/show_all_experiment/', {}, function(data){
		$('#microbe_experiment').html(data);
		$('#selected_microbe_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#env_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/environment/suggest_env_experiment/', {suggestion: query}, function(data){
		$('#env_experiment').html(data);
		$('#selected_env_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_env_experiment').click(function(){
	$.get('/lab/data/environment/show_all_experiment/', {}, function(data){
		$('#env_experiment').html(data);
		$('#selected_env_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#tissue_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/tissue/suggest_tissue_experiment/', {suggestion: query}, function(data){
		$('#tissue_experiment').html(data);
		$('#selected_tissue_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_tissue_experiment').click(function(){
	$.get('/lab/data/tissue/show_all_experiment/', {}, function(data){
		$('#tissue_experiment').html(data);
		$('#selected_tissue_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#maize_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/maize/suggest_maize_experiment/', {suggestion: query}, function(data){
		$('#maize_experiment').html(data);
		$('#selected_maize_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_maize_experiment').click(function(){
	$.get('/lab/data/maize/show_all_experiment/', {}, function(data){
		$('#maize_experiment').html(data);
		$('#selected_maize_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#sample_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/sample/suggest_sample_experiment/', {suggestion: query}, function(data){
		$('#sample_experiment').html(data);
		$('#selected_sample_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_sample_experiment').click(function(){
	$.get('/lab/data/sample/show_all_experiment/', {}, function(data){
		$('#sample_experiment').html(data);
		$('#selected_sample_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#culture_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/culture/suggest_culture_experiment/', {suggestion: query}, function(data){
		$('#culture_experiment').html(data);
		$('#selected_culture_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_culture_experiment').click(function(){
	$.get('/lab/data/culture/show_all_experiment/', {}, function(data){
		$('#culture_experiment').html(data);
		$('#selected_culture_experiment').dataTable({
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

$('#dna_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/dna/suggest_dna_experiment/', {suggestion: query}, function(data){
		$('#dna_experiment').html(data);
		$('#selected_dna_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_dna_experiment').click(function(){
	$.get('/lab/data/dna/show_all_experiment/', {}, function(data){
		$('#dna_experiment').html(data);
		$('#selected_dna_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#plate_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/plate/suggest_plate_experiment/', {suggestion: query}, function(data){
		$('#plate_experiment').html(data);
		$('#selected_plate_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_plate_experiment').click(function(){
	$.get('/lab/data/plate/show_all_experiment/', {}, function(data){
		$('#plate_experiment').html(data);
		$('#selected_plate_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#well_experimentsuggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/data/well/suggest_well_experiment/', {suggestion: query}, function(data){
		$('#well_experiment').html(data);
		$('#selected_well_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_well_experiment').click(function(){
	$.get('/lab/data/well/show_all_experiment/', {}, function(data){
		$('#well_experiment').html(data);
		$('#selected_well_experiment').dataTable({
			"searching": false,
			"scrollY": "300px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#show_all_measurement_experiment').click(function(){
	$('#suggested_measurement_experiments').css('display', 'block');
	$('#selected_measurement_experiments').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/data/measurement/show_all_experiment/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "obs_tracker__experiment__name"},
		{ "mData": "obs_tracker__experiment__field__field_name"},
		{ "mData": "measurement_parameter__parameter"},
		],
	});
});

$('#measurement_experimentsuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_measurement_experiments').css('display', 'none'); }
	else { $('#suggested_measurement_experiments').css('display', 'block'); }
	$('#selected_measurement_experiments').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": {
			"url": "/lab/data/measurement/suggest_measurement_experiment/",
			"type": 'POST',
			"data": {'suggestion':query},
			beforeSend: function(xhr, settings) {
				var csrftoken = getCookie('csrftoken');
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		},
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "obs_tracker__experiment__name"},
		{ "mData": "obs_tracker__experiment__field__field_name"},
		{ "mData": "measurement_parameter__parameter"},
		],
	});
});

$('#select_measurement_experiment_form_submit').click(function(){
	var experiments = [];
	$("input[name='checkbox_measurement_experiment']:checked").each(function() {
		experiments.push($(this).val());
	});
	$.ajax({
		"url": "/lab/data/measurement/select_measurement_experiment/",
		"type": "POST",
		"data": {'experiments': JSON.stringify(experiments)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting experiments!");
		}
	});
});

$('#clear_selected_measurement_experiments').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_measurement_experiment_id_list/",
		success: function() {
			$.ajax({
				"url": "/lab/checkbox_clear/checkbox_measurement_experiment/",
				success: function() {
					location.reload(true);
				},
				error: function() {
					alert("Error clearing selected measurements!");
				}
			});
		},
		error: function() {
			alert("Error clearing selected measurement ids!");
		}
	});
});

$('#measurement_parametersuggestion').keyup(function(){
	var query = $(this).val();
	if (query == '') { $('#suggested_measurement_parameters').css('display', 'none'); }
	else { $('#suggested_measurement_parameters').css('display', 'block'); }
	$('#selected_measurement_parameters').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": {
			"url": "/lab/data/measurement/suggest_measurement_parameter/",
			"type": 'POST',
			"data": {'suggestion':query},
			beforeSend: function(xhr, settings) {
				var csrftoken = getCookie('csrftoken');
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		},
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "measurement_parameter__parameter"},
		{ "mData": "measurement_parameter__parameter_type"},
		{ "mData": "obs_tracker__experiment__name"},
		],
	});
});

$('#show_all_measurement_parameter').click(function(){
	$('#suggested_measurement_parameters').css('display', 'block');
	$('#selected_measurement_parameters').dataTable({
		"destroy": true,
		"searching": false,
		"scrollY": "300px",
		"scrollCollapse": true,
		"paginate": false,
		"ajax": "/lab/data/measurement/show_all_parameter/",
		"deferRender": true,
		"aoColumns": [
		{ "mData": "input"},
		{ "mData": "measurement_parameter__parameter"},
		{ "mData": "measurement_parameter__parameter_type"},
		{ "mData": "obs_tracker__experiment__name"},
		],
	});
});

$('#select_measurement_parameter_form_submit').click(function(){
	var parameters = [];
	$("input[name='checkbox_measurement_parameter']:checked").each(function() {
		parameters.push($(this).val());
	});
	$.ajax({
		"url": "/lab/data/measurement/select_measurement_parameter/",
		"type": "POST",
		"data": {'parameters': JSON.stringify(parameters)},
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error selecting parameters!");
		}
	});
});

$('#clear_select_meaurement_parameters').click(function(){
	$.ajax({
		"url": "/lab/checkbox_clear/checkbox_measurement_parameter/",
		success: function() {
			location.reload(true);
		},
		error: function() {
			alert("Error clearing selected parameters!");
		}
	});
});

$('#clear_plant_experiment').click(function(){
	$.get('/lab/data/plant/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_row_experiment').click(function(){
	$.get('/lab/data/row/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_tissue_experiment').click(function(){
	$.get('/lab/data/tissue/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_plate_experiment').click(function(){
	$.get('/lab/data/plate/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_well_experiment').click(function(){
	$.get('/lab/data/well/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_culture_experiment').click(function(){
	$.get('/lab/data/culture/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_dna_experiment').click(function(){
	$.get('/lab/data/dna/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_microbe_experiment').click(function(){
	$.get('/lab/data/microbe/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_env_experiment').click(function(){
	$.get('/lab/data/environment/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_maize_experiment').click(function(){
	$.get('/lab/data/maize/checkbox_clear/', {}, function(data){
		$('body').html(data);
	});
});

$('#clear_sample_experiment').click(function(){
	$.get('/lab/data/sample/checkbox_clear/', {}, function(data){
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
		$('#selected_stocks').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
		});
		$('#seed_inventory_datatable').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"ajax": "/lab/datatable/seed_inventory/",
			"deferRender": true,
			"aoColumns": [
				{ "mData": "input"},
				{ "mData": "seed_id",
					"mRender": function (data, type, full) {
						return '<a href=/lab/stock/' + full.id + '/>' + full.seed_id + '</a>';
					}
				},
		  	{ "mData": "cross_type"},
		  	{ "mData": "pedigree"},
		  	{ "mData": "population"},
		  	{ "mData": "status"},
				{ "mData": "collector",
					"mRender": function (data, type, full) {
						return '<a href=/lab/profile/' + full.collector + '/>' + full.collector + '</a>';
					}
				},
				{ "mData": "comments"},
		  ],
		});

		$('#isolatestock_inventory_datatable').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"ajax": "/lab/datatable/isolatestock_inventory/",
			"deferRender": true,
			"aoColumns": [
			  { "mData": "input"},
			  { "mData": "isolatestock_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/isolatestock/' + full.id + '/>' + full.isolatestock_id + '</a>';
			    }
		    },
		    { "mData": "isolatestock_name"},
		    { "mData": "disease_name",
				  "mRender": function (data, type, full) {
					  return '<a href=/lab/disease_info/' + full.disease_id + '/>' + full.disease_name + '</a>';
				  }
				},
		    { "mData": "plant_organ"},
		    { "mData": "genus"},
		    { "mData": "alias"},
		    { "mData": "race"},
		    { "mData": "subtaxa"},
	      { "mData": "comments"},
	    ],
    });

		$('#glycerol_inventory_datatable').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"ajax": "/lab/datatable/glycerol_stock_inventory/",
			"deferRender": true,
			"aoColumns": [
			  { "mData": "glycerol_stock_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/glycerol_stock/' + full.id + '/>' + full.glycerol_stock_id + '</a>';
			    }
		    },
			  { "mData": "experiment_name",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/experiment/' + full.experiment_name + '/>' + full.experiment_name + '</a>';
			    }
		    },
			  { "mData": "field_name",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/field/' + full.field_id + '/>' + full.field_name + '</a>';
			    }
		    },
			  { "mData": "isolatestock_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/isolatestock/' + full.isolatestock_table_id + '/>' + full.isolatestock_id + '</a>';
			    }
		    },
			  { "mData": "dna_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/dna/' + full.obs_dna_id + '/>' + full.dna_id + '</a>';
			    }
		    },
			  { "mData": "location_name",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/location/' + full.location_id + '/>' + full.location_name + '</a>';
			    }
		    },
		    { "mData": "stock_date"},
		    { "mData": "extract_color"},
		    { "mData": "organism"},
		    { "mData": "username",
		      "mRender": function (data, type, full) {
			      return '<a href=/lab/profile/' + full.username + '/>' + full.username + '</a>';
		      }
	      },
				{ "mData": "comments"},
			],
		});

		$('#measurement_data_datatable').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"ajax": "/lab/datatable/measurement_data/",
			"deferRender": true,
			"aoColumns": [
				{ "mData": "experiment",
					"mRender": function (data, type, full) {
						return '<a href=/lab/experiment/' + full.experiment_name + '/>' + full.experiment_name + '</a>';
					}
				},
				{ "mData": "obs_id",
					"mRender": function (data, type, full) {
						return '<a href=' + full.obs_url + '>' + full.obs_id + '</a>';
					}
				},
				{ "mData": "username",
					"mRender": function (data, type, full) {
						return '<a href=/lab/profile/' + full.username + '/>' + full.username + '</a>';
					}
				},
				{ "mData": "time_of_measurement"},
				{ "mData": "parameter_type"},
				{ "mData": "parameter_name",
				  "mRender": function (data, type, full) {
						return '<a href=/lab/measurement_parameter/' + full.parameter_id + '/>' + full.parameter_name + '</a>';
					}
				},
				{ "mData": "value"},
				{ "mData": "unit_of_measure"},
				{ "mData": "trait_id_buckler"},
				{ "mData": "comments"},
			],
		});

});

$(document).ready(function() {
	$('.selected_stocks').dataTable({
		"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
	});
} );

$(document).ready(function() {
		$('#selected_legacy_stock_child_row').dataTable({
			"searching": false,
			"scrollY": "500px",
			"scrollCollapse": true,
			"paginate": false
			});
} );

$(document).ready(function() {
	$('.datatable').dataTable({
	});
} );

function toggle(source) {
	checkboxes = document.getElementsByName('checkbox_stock');
	for(var i=0, n=checkboxes.length;i<n;i++) {
		checkboxes[i].checked = source.checked;
	}
}

function toggle_isolatestocks(source) {
	checkboxes = document.getElementsByName('checkbox_isolatestocks');
	for(var i=0, n=checkboxes.length;i<n;i++) {
		checkboxes[i].checked = source.checked;
	}
}

$('#seedidsearch').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/seed_inventory/seed_id_search/', {suggestion: query}, function(data){
		$('#seed_id_search_results').html(data);
		$('#seed_id_search_table').dataTable({
			"searching": false,
			"scrollY": "200px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#isolatestockidsearch').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/iso_inventory/isolatestock_id_search/', {suggestion: query}, function(data){
		$('#isolatestock_id_search_results').html(data);
		$('#isolatestock_id_search_table').dataTable({
			"searching": false,
			"scrollY": "200px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

$('#sidebarsearch').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/lab/sidebar_search/', {suggestion: query}, function(data){
		$('#sidebar_search_results').html(data);
		$('#sidebar_search_results_table').dataTable({
			"searching": false,
			"scrollY": "200px",
			"scrollCollapse": true,
			"paginate": false
		});
	});
});

var frm = $('#query_builder_options_form');
frm.submit(function () {
	$.ajax({
		type: frm.attr('method'),
		url: frm.attr('action'),
		data: frm.serialize(),
		success: function (data) {
			$("#query_builder_fields").html(data);
		},
		error: function(data) {
			$("#query_builder_fields").html("Something went wrong!");
		}
	});
	return false;
});

var query_builder_fields_form = $('#query_builder_fields_form');
query_builder_fields_form.submit(function () {
	$.ajax({
		type: query_builder_fields_form.attr('method'),
		url: query_builder_fields_form.attr('action'),
		data: query_builder_fields_form.serialize(),
		success: function (data) {
			$("#query_builder_results").html(data);
		},
		error: function(data) {
			$("#query_builder_results").html("Something went wrong!");
		}
	});
	return false;
});
