
$(document).ready(function(){
  if ($('#overview_chart').length > 0 ) {

  $.ajax({
    dataType: "json",
    url: "/lab/data/genotype/browse/plot/",
    success: function(data) {
      //console.log(data);
      var margin = {top: 20, right: 20, bottom: 30, left: 40},
      width = 1280 - margin.left - margin.right,
      height = 600 - margin.top - margin.bottom;

      var x = d3.scale.linear()
      .range([0, width]);

      var y = d3.scale.linear()
      .range([height, 0]);

      var color = d3.scale.category10();

      var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

      var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

      var svg = d3.select("#overview_chart").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      data.data.forEach(function(d) {
        d.chromosome = +d.chromosome;
        d.position = +d.position;
      });

      x.domain(d3.extent(data.data, function(d) { return d.position; })).nice();
      y.domain(d3.extent(data.data, function(d) { return d.chromosome; })).nice();

      svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Position (bp)");

      svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Chromosome")

      svg.selectAll(".dot")
      .data(data.data)
      .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 3.5)
      .attr("cx", function(d) { return x(d.position); })
      .attr("cy", function(d) { return y(d.chromosome); })
      .style("fill", function(d) { return color(d.type); })
      .on("mouseover", function(d) {
        d3.select(this).style("fill", "white");
        $(this).popover({html:true, title:d.name, placement:'right', container:'body', content: 'Chromosome: '+d.chromosome+'<br/>Type: '+d.type+'<br/>Position (bp): '+d.position}).popover('show');
      })
      .on("mouseout",  function(d) {
        d3.select(this).style("fill", color(d.type));
        $(this).popover("hide");
      });

      var legend = svg.selectAll(".legend")
      .data(color.domain())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

      legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

      legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });

    }
  });

  }

});
