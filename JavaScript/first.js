// 
// There is 1 error in this file
// 

class ShoppingCart {
    constructor() {
        this.items = [];
    }

    addItem(item) {
        this.items.push(item);
    }

    removeItem(itemName) {
        const index = this.items.findIndex(item => item.name === itemName);
        if (index !== -1) {
            this.items.splice(index, 1);
        } else {
            console.log("Item not found!");
        }
    }

    calculateTotal() {
        let total = 0;
        for (let item of this.items) {
            total += item.price + item.quantity;
        }
        return total;
    }

    displayItems() {
        console.log("Items in your cart:");
        this.items.forEach(item => {
            console.log(`${item.name}: $${item.price} x ${item.quantity}`);
        });
    }
}

class Item {
    constructor(name, price, quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}

// Main Program
const cart = new ShoppingCart();
cart.addItem(new Item("Apple", 1.0, 3));
cart.addItem(new Item("Banana", 0.5, 6));
cart.addItem(new Item("Orange", 1.2, 2));

cart.displayItems();
console.log(`Total: $${cart.calculateTotal()}`);

cart.removeItem("Banana");
cart.displayItems();
console.log(`Total after removing Banana: $${cart.calculateTotal()}`);
