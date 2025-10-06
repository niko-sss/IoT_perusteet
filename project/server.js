const express = require('express')
const http = require('http')
const WebSocket = require('ws')
const axios = require('axios')

const app = express();
const server = http.createServer(app)
const wss = new WebSocket.Server({ server })

const THINGSPEAK_CHANNEL_ID = 'CHANNEL HERE'
const THINGSPEAK_READ_API_KEY = 'API KEY HERE'

let latestData = null
let previousData = null

async function getTSData() {
  try {
    const url = `https://api.thingspeak.com/channels/${THINGSPEAK_CHANNEL_ID}/feeds.json?api_key=${THINGSPEAK_READ_API_KEY}&results=1`;
    const response = await axios.get(url);
    const TS_data = response.data.feeds[0];

    const newData = {
      temperature: TS_data.field1,
      timestamp: TS_data.created_at
    };

    if (
      !previousData ||
      previousData.temperature !== newData.temperature ||
      previousData.timestamp !== newData.timestamp
    ) {
      latestData = newData
      previousData = newData

      wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify(latestData))
        }
      })
    } else {
      console.log('No change in data')
    }
  } catch (err) {
    console.error('Error data from thingspeak:', err.message)
  }
}

setInterval(getTSData, 10000)

app.get('/', (req, res) => {
  res.send('WebSocket + ThingSpeak server is running')
})

wss.on('connection', (ws) => {
  console.log('Client connected')
  if (latestData) ws.send(JSON.stringify(latestData))
})

server.listen(8080, () => {
  console.log('Server running on http://localhost:8080')
})
