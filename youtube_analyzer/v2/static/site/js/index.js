var data = [
    {
        "week": "W6 2011",
        "c56bgh": 7,
        "tr56gc": 89,
        "c56yg": 5,
        "fr566h": 8
    },
    {
        "week": "W7 2011",
        "c56bgh": 77,
        "tr56gc": 79,
        "c56yg": 5,
        "fr566h": 9
    }
];

var margin = {
    top: 20,
    right: 20,
    bottom: 40,
    left: 60
};
            
width = 500 - margin.left - margin.right;
height = 400 - margin.top - margin.bottom;
that = this;


var x = d3.scale.ordinal().rangeRoundBands([0, width], .2);

var y = d3.scale.linear().rangeRound([height, 0]);

var color = d3.scale.category20();

var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

var svg = d3.select(".chart").append("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom).append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

color.domain(d3.keys(data[0]).filter(function (key) {
    return key !== "week";
}));

data.forEach(function(d){
        var y0 = 0;

        d.rates = color.domain().map(function (name) {
            console.log();;
            return {
                name: name,
                y0: y0,
                y1: y0 += +d[name],
                amount: d[name]
            };
        });
        d.rates.forEach(function (d) {
            d.y0 /= y0;
            d.y1 /= y0;
        });

        console.log(data);
    });

    data.sort(function (a, b) {
        return b.rates[0].y1 - a.rates[0].y1;
    });

    x.domain(data.map(function (d) {
        return d.interest_rate;
    }));

    svg.append("g").attr("class", "x axis").attr("transform", "translate(0," + height + ")").call(xAxis);

    svg.append("g").attr("class", "y axis").call(yAxis);

    var week = svg.selectAll(".week").data(data).enter().append("g").attr("class", "e").attr("transform", function (d) {
        return "translate(" + x(d.interest_rate) + ",0)";
    });

    interest_rate.selectAll("rect").data(function (d) {
        return d.rates;
    }).enter().append("rect").attr("width", x.rangeBand()).attr("y", function (d) {
        return y(d.y1);
    }).attr("height", function (d) {
        return y(d.y0) - y(d.y1);
    }).style("fill", function (d) {
        return color(d.name);
    }).on('mouseover', function (d) {
        var total_amt;
        total_amt = d.amount;



        console.log('----');
        d3.select(".chart-tip").style('opacity', '1').html('Amount: <strong>$' + that.numberWithCommas(total_amt.toFixed(2)) + '</strong>');

    }).on('mouseout', function () {
        d3.select(".chart-tip").style('opacity', '0');
    });


