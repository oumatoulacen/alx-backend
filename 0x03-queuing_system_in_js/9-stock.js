import kue from 'kue';
import { createClient } from 'redis';
import { promisify } from "util";

const express = require('express');

const client = createClient();

const app = express();
app.use(express.json());

const listProducts = [
    { itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4, },
    { itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10, },
    { itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2, },
    { itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5, },
];


const getAsync = promisify(client.get).bind(client);

function getItemById(id) {
    return listProducts.find(product => product.itemId === id);
}

function reserveStockById(id, stock) {
  client.set(`item.${id}`, stock);
}

function getCurrentReservedStockById(id) {
    return getAsync(`item.${id}`);
}
// reserveStockById(1, 3);

// GET /
app.get('/', (req, res) => {
    res.send('Welcome to our stock!');
});

// GET /list_products
app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) res.json({ status: "Product not found" });
    else {
        const currentQuantity = await getCurrentReservedStockById(itemId);
        item["currentQuantity"] = (currentQuantity !== null ) ? currentQuantity : item["initialAvailableQuantity"];
        res.json(item);
    }
});

// GET /reserve_product/:id
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) res.json({ status: "Product not found" });
    else {
        if (item["availableQuantity"] <= 0) {
            res.json({"status":"Not enough stock available","itemId":itemId});
        } else {
            reserveStockById(itemId, 1);
            res.json({"status":"Reservation confirmed","itemId":itemId});
        }
    }
});


// start the server
app.listen(1245, () => {
  console.log('Server started (http://localhost:1245)!');
});
