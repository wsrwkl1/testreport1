var chart;

var chartData = [{
	version: "4.1.1",
	Failed: 3,
	Passed: 7
}, {
	version: "4.1.7",
	Failed: 2,
	Passed: 8
}, {
	version: "4.1.8",
	Failed: 1,
	Passed: 9
}];


AmCharts.ready(function () {
	// SERIAL CHART
	chart = new AmCharts.AmSerialChart();
	chart.dataProvider = chartData;
	chart.categoryField = "version";
	chart.color = "#FFFFFF";
	chart.fontSize = 14;
	chart.startDuration = 1;
	chart.plotAreaFillAlphas = 0.2;
	// the following two lines makes chart 3D
	chart.angle = 30;
	chart.depth3D = 60;

	// AXES
	// category
	var categoryAxis = chart.categoryAxis;
	categoryAxis.gridAlpha = 0.2;
	categoryAxis.gridPosition = "start";
	categoryAxis.gridColor = "#FFFFFF";
	categoryAxis.axisColor = "#FFFFFF";
	categoryAxis.axisAlpha = 0.5;
	categoryAxis.dashLength = 5;

	// value
	var valueAxis = new AmCharts.ValueAxis();
	valueAxis.stackType = "3d"; // This line makes chart 3D stacked (columns are placed one behind another)
	valueAxis.gridAlpha = 0.2;
	valueAxis.gridColor = "#FFFFFF";
	valueAxis.axisColor = "#FFFFFF";
	valueAxis.axisAlpha = 0.5;
	valueAxis.dashLength = 5;
	valueAxis.title = "用例条数"
	valueAxis.titleColor = "#FFFFFF";
	//valueAxis.unit = "%";
	chart.addValueAxis(valueAxis);

	// GRAPHS         
	// first graph
	var graph1 = new AmCharts.AmGraph();
	graph1.title = "Fail";
	graph1.valueField = "Failed";
	graph1.type = "column";
	graph1.lineAlpha = 0;
	graph1.lineColor = "#FF0033";
	graph1.fillAlphas = 1;
	graph1.balloonText = "在[[category]]版本中Failed的case条数为：[[value]]";
	chart.addGraph(graph1);

	// second graph
	var graph2 = new AmCharts.AmGraph();
	graph2.title = "Pass";
	graph2.valueField = "Passed";
	graph2.type = "column";
	graph2.lineAlpha = 0;
	graph2.lineColor = "#009966";
	graph2.fillAlphas = 1;
	graph2.balloonText = "在[[category]]版本中Passed的case条数为：[[value]]";
	chart.addGraph(graph2);

	chart.write("chartdiv");
});
