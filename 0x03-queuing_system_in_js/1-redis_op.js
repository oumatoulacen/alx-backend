import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');


// with redis async/await server
// import { createClient, print } from 'redis';

// const client = createClient();
// client.on('error', err => console.log('Redis Client Error', err));
// client.on('connect', () => console.log('Redis client connected to the server'));

// client.connect();

// async function setNewSchool(schoolName, value) {
//     try {
//         const replay = await client.set(schoolName, value);
//         console.log("Replay: " + replay);
//     } catch (err)
//     {
//         console.log(err);
//     }
// }

// async function displaySchoolValue(schoolName) {
//     const value = await client.get(schoolName);
//     console.log(value);
// }


// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFrancisco', '100');
// displaySchoolValue('HolbertonSanFrancisco');