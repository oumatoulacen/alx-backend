import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
    try {
        const result=  await getAsync(schoolName);
        console.log(result);
    } catch (err) {
        console.log(err);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
