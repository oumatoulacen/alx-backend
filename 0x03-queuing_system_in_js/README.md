# 0x03-queuing_system_in_js

## Installation

### Start a redis via docker

docker run -p 6379:6379 -it redis/redis-stack-server:latest

### To install node-redis, simply

```npm install redis```

## resources

- kue:
    <https://github.com/Automattic/kue?tab=readme-ov-file#processing-concurrency>

- node-redis:
    <https://github.com/redis/node-redis>


Let's go through each of these topics step-by-step.

### 1. Running a Redis Server on Your Machine

**Installing Redis:**

- **On macOS:** You can use Homebrew to install Redis.
  ```bash
  brew install redis
  ```

- **On Ubuntu/Debian:**
  ```bash
  sudo apt update
  sudo apt install redis-server
  ```

- **On Windows:** You can download the MSI installer from the [Redis website](https://redis.io/download) or use Windows Subsystem for Linux (WSL) to install it.

**Starting the Redis server:**
```bash
redis-server
```

**Stopping the Redis server:**
```bash
redis-cli shutdown
```

### 2. Running Simple Operations with the Redis Client

**Connecting to Redis:**
```bash
redis-cli
```

**Basic Commands:**
```bash
# Set a key-value pair
SET key "value"

# Get the value of a key
GET key

# Increment a key's value
INCR key

# Decrement a key's value
DECR key

# Delete a key
DEL key

# Check if a key exists
EXISTS key

# List all keys
KEYS *
```

### 3. Using Redis with Node.js for Basic Operations

**Install the Redis package:**
```bash
npm install redis
```

**Basic Usage:**
```javascript
const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
    console.log('Connected to Redis');
});

// Setting a key
client.set('key', 'value', redis.print);

// Getting a key
client.get('key', (err, reply) => {
    if (err) throw err;
    console.log(reply);
});

// Incrementing a key
client.incr('counter', (err, reply) => {
    if (err) throw err;
    console.log(reply);
});
```

### 4. Storing Hash Values in Redis

**Using the Redis client:**
```javascript
// Setting a hash
client.hset('user:1000', 'name', 'John Doe', 'email', 'john.doe@example.com', redis.print);

// Getting all fields and values in a hash
client.hgetall('user:1000', (err, reply) => {
    if (err) throw err;
    console.log(reply);
});

// Setting multiple fields
client.hmset('user:1001', 'name', 'Jane Doe', 'email', 'jane.doe@example.com', redis.print);
```

### 5. Dealing with Async Operations with Redis

You can use Promises or async/await for dealing with asynchronous operations in Redis.

**Using Promises:**
```javascript
const { promisify } = require('util');

const getAsync = promisify(client.get).bind(client);

getAsync('key').then(reply => {
    console.log(reply);
}).catch(err => {
    console.error(err);
});
```

**Using async/await:**
```javascript
(async () => {
    try {
        const value = await getAsync('key');
        console.log(value);
    } catch (err) {
        console.error(err);
    }
})();
```

### 6. Using Kue as a Queue System

**Install Kue:**
```bash
npm install kue
```

**Basic Usage:**
```javascript
const kue = require('kue');
const queue = kue.createQueue();

queue.on('job enqueue', (id, type) => {
    console.log(`Job ${id} got queued of type ${type}`);
});

queue.on('job complete', (id, result) => {
    console.log(`Job ${id} completed with result ${result}`);
});

// Creating a job
const job = queue.create('email', {
    title: 'Welcome email for new user',
    to: 'user@example.com',
    template: 'welcome-email'
}).save((err) => {
    if (!err) console.log(job.id);
});

// Processing jobs
queue.process('email', (job, done) => {
    sendEmail(job.data.to, job.data.template, done);
});
```

### 7. Building a Basic Express App Interacting with a Redis Server

**Setting up the project:**
```bash
mkdir redis-express-app
cd redis-express-app
npm init -y
npm install express redis
```

**Basic Express Server:**
```javascript
const express = require('express');
const redis = require('redis');
const app = express();
const client = redis.createClient();

client.on('connect', () => {
    console.log('Connected to Redis');
});

app.get('/', (req, res) => {
    client.get('visits', (err, visits) => {
        if (err) throw err;
        res.send(`Number of visits is ${visits}`);
        client.set('visits', parseInt(visits) + 1);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

### 8. Building a Basic Express App Interacting with a Redis Server and Queue

**Install necessary packages:**
```bash
npm install kue
```

**Updating the Express Server:**
```javascript
const kue = require('kue');
const queue = kue.createQueue();

app.get('/enqueue', (req, res) => {
    const job = queue.create('email', {
        title: 'Welcome email for new user',
        to: 'user@example.com',
        template: 'welcome-email'
    }).save((err) => {
        if (!err) res.send(`Job id: ${job.id}`);
    });
});

queue.process('email', (job, done) => {
    // Simulate sending email
    console.log(`Sending email to ${job.data.to}`);
    setTimeout(() => {
        console.log(`Email sent to ${job.data.to}`);
        done();
    }, 3000);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

This should give you a good starting point for working with Redis, Node.js, and Express, as well as using Kue for job queuing. Let me know if you need more details on any specific part.