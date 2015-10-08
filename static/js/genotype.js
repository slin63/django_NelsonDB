
$(document).ready(function(){

  $.ajax({
    dataType: "json",
    url: "/lab/data/genotype/browse/plot/",
    success: function(data) {
      console.log(data);
      $('#overview_chart').jqplot([data.qtl, data.markers, data.expression],{
        seriesDefaults:{
          renderer:$.jqplot.BlockRenderer
        },
        legend:{
          renderer: $.jqplot.EnhancedLegendRenderer,
          show:true
        },
        series: [
        {},
        {rendererOptions: {
          css:{background:'#A1EED6'}
        }},
        {rendererOptions: {
          css:{background:'#D3E4A0'}
        }}
        ],
        axes: {
          //bp positions on chromosome
          xaxis: {
            min:0,
            max: 300000000
          },
          //chromosomes
          yaxis: {
            min: 1,
            max: 10
          }
        }
      });
    }
  });

});
