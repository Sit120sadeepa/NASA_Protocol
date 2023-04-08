const dtn = require('dtn-bp');

// Set up connection to the BP daemon
const connection = dtn({ daemon: 'localhost' });

// Define the destination endpoint
const destination = {
  eid: 'dtn://destination-node',
  scheme: 'dtn'
};

// Define the source endpoint
const source = {
  eid: 'dtn://source-node',
  scheme: 'dtn'
};

// Define the payload for the message
const payload = Buffer.from('Hello, world!');

// Define the message options
const options = {
  priority: 1,
  report: true,
  lifetime: 3600
};

// Send the message
connection.send(destination, source, payload, options, (err, report) => {
  if (err) {
    console.error(err);
    return;
  }
  
  console.log(`Message sent: ${report}`);
});
