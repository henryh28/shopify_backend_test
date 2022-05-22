
// Navbar button to go to route "/"
document.querySelector("#btn-home").addEventListener("click", () => {
    window.location = "/";
})

// Navbar button to create a warehouse
document.querySelector("#btn-create-warehouse").addEventListener("click", () => {
    window.location = "/create_warehouse";
})

// Navbar button to create an item
document.querySelector("#btn-create-item").addEventListener("click", () => {
    window.location = "/create_item";
})

// Navbar button to view all items
document.querySelector("#view-items").addEventListener("click", () => {
    window.location = "/view_items";
})


