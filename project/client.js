const socket = new WebSocket('ws://localhost:8080')

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(initChart);

let chartData
let chart
let options


socket.onopen = () => {
    document.getElementById('connection').innerText += 'Connected to server\n'
}

function initChart() {
    chartData = new google.visualization.DataTable()
    chartData.addColumn('datetime', 'Time')
    chartData.addColumn('number', 'Temperature')
    
    options = {
        title: 'Temperature change overtime in celcius (°C)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    
    chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
    chart.draw(chartData, options);
}

socket.onmessage = event => {
    const incomingData = JSON.parse(event.data)
    document.getElementById('log').innerText += 'Server: ' + event.data + '\n'
    const date = new Date(incomingData.timestamp)
    console.log(`${date.getUTCHours()}:${date.getUTCMinutes()}:${date.getUTCSeconds()}`)
    console.log(incomingData.temperature, '°C')
    if (parseFloat(incomingData.temperature) > 38) {
        document.documentElement.style.backgroundColor = 'salmon'
    } else {
        document.documentElement.style.backgroundColor = ''
    }
    chartData.addRow([date, parseFloat(incomingData.temperature)])
    chart.draw(chartData, options)
}