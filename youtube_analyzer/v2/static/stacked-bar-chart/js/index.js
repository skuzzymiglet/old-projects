var data = [
    {
        "week": 'W4 2017',
        "cfrg56": 1,
        "yh6u57": 1,
        "vgh5f66": 1,
        "kooci": 1
    },
    {
        "week": 'W5 2017',
        "nc6g56": 1,
        "dh5j67": 1,
        "ng67vg6": 1,
        "reet": 1
    },
    {
        "week": 'W6 2017',
        "nc656": 1,
        "dhkjgefcrygnfbkn7": 1,
        "ncrumblesvg6": 1,
        "kajjoo": 1,
        "poo": 1
    }
];

var margin = {
        top: 180,
        right: 50,
        bottom: 30,
        left: 0
    },
    width = 350 - margin.left - margin.right,
    height = 800 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], 0.5);

var y = d3.scale.linear()
    .rangeRound([height, 0]);

var color = d3.scale.category20();

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var dataIntermediate = data.map(function (d, index) {// d = data element, c = week
    to_return = Object.keys(d).map(function (k) {
        if (k !== "week") {
            return {
                x: d.week,
                y: d[k],
                y0: index
            };
        }
    });
    to_return.shift();
    return to_return;
});

console.log(dataIntermediate)

var dataStackLayout = d3.layout.stack()(dataIntermediate);

x.domain(data.map(function (z) {
    return z.week;
}));

y.domain([0,
        d3.sum(data,
            function (e) {
                var key;
                for (key in e) {
                    if (!(key == "week")) {
                        return e[key];
                    }
                }
            })
        ])
    .nice();

console.log(y.domain)

var layer = svg.selectAll(".stack")
    .data(dataStackLayout)
    .enter().append("g")
    .attr("class", "stack")
    .style("fill", function (d, i) {
        return color(i);
    });

var idPool = [];

data.forEach(function (x) {
    Object.keys(x).forEach(function (y) {
        if (!(y == "week")) {
            idPool.push(y);
        }
    });
});


layer.selectAll("rect")
    .data(function (d) {
        return d;
    })
    .enter().append("rect")
    .attr("x", function (d) {
        return x(d.x);
    })
    .attr("y", function (d, i) {
        return y(d.y + i);
    })
    .attr("height", function (d) {
        console.log(y(d.y0) - y(d.y + d.y0));
        return y(d.y0) - y(d.y + d.y0);
    })
    .attr("width", x.rangeBand());

layer.selectAll("rect")
    .attr("id", function (a, index) {
        return [this.x.baseVal.value, this.y.baseVal.value * -1]
    });

svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

$("p").each(function (index, f) {
    f[index].attr("id", idPool[index])
});
