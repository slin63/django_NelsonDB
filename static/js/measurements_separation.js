
$(document).ready(function(){
  if ($('#separations_chart').length > 0 ) {
  $.ajax({
    dataType: "json",
    url: "/lab/data/measurement/"+$('#measurement_experiment_name').val()+"/separations",
    success: function(data) {
      console.log(data);
      var margin = {top: 20, right: 20, bottom: 30, left: 80},
      width = 1280 - margin.left - margin.right,
      height = 600 - margin.top - margin.bottom;

      var x = d3.scale.linear()
      .range([80, width-80]);

      var y = d3.scale.linear()
      .range([height, 0]);

      var color = d3.scale.category10();

      var xScale = d3.scale.ordinal()
      .domain(data.data.map(function (d) {return d.sample_type; }))
      .rangeRoundBands([margin.left, width], 0.05);

      var xAxis = d3.svg.axis().scale(xScale).orient("bottom");

      var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

      var svg = d3.select("#separations_chart").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      data.data.forEach(function(d) {
        d.m_value = +d.m_value;
        d.sample_type = +d.sample_type;
      });

      x.domain(d3.extent(data.data, function(d) { return d.sample_type_number; })).nice();
      y.domain(d3.extent(data.data, function(d) { return d.m_value; })).nice();

      svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Sample Type");

      svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("AF (ppb)")

      svg.selectAll(".dot")
      .data(data.data)
      .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 3.5)
      .attr("cx", function(d) { return x(d.sample_type_number); })
      .attr("cy", function(d) { return y(d.m_value); })
      .style("fill", function(d) { return color(d.sample_type_number); })
      .on("mouseover", function(d) {
        d3.select(this).style("fill", "white");
        $(this).popover({html:true, title:d.sample_id, placement:'right', container:'body', content: 'Value: '+d.m_value+'<br/>Parameter: '+d.parameter_type+'<br/>Sample Type: '+d.sample_type_number}).popover('show');
      })
      .on("mouseout",  function(d) {
        d3.select(this).style("fill", color(d.sample_type_number));
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
