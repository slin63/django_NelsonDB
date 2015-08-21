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

		$('#isolate_inventory_datatable').dataTable({
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"ajax": "/lab/datatable/isolate_inventory/",
			"deferRender": true,
			"aoColumns": [
			  { "mData": "input"},
			  { "mData": "isolate_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/isolate/' + full.id + '/>' + full.isolate_id + '</a>';
			    }
		    },
		    { "mData": "isolate_name"},
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
			  { "mData": "isolate_id",
			    "mRender": function (data, type, full) {
				    return '<a href=/lab/isolate/' + full.isolate_table_id + '/>' + full.isolate_id + '</a>';
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

function toggle(source) {
	checkboxes = document.getElementsByName('checkbox_stock');
	for(var i=0, n=checkboxes.length;i<n;i++) {
		checkboxes[i].checked = source.checked;
	}
}

function toggle_isolates(source) {
	checkboxes = document.getElementsByName('checkbox_isolates');
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
