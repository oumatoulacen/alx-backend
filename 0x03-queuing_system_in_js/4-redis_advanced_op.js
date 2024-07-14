import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

//set hash key-value in HolbertonSchools list
// client.hset('HolbertonSchools', 'Portland', '50', print);
// client.hset('HolbertonSchools', 'Seattle', '80', print);
// client.hset('HolbertonSchools', 'New York', '20', print);
// client.hset('HolbertonSchools', 'Bogota', '20', print);
// client.hset('HolbertonSchools', 'Cali', '40', print);
// client.hset('HolbertonSchools', 'Paris', '2', print);

client.hmset('HolbertonSchools',
  'Portland', '50',
  'Seattle', '80',
  'New York', '20',
  'Bogota', '20',
  'Cali', '40',
  'Paris', '2', print);

// retrieve all elements stored in HolbertonSchools list
client.hgetall('HolbertonSchools', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});
