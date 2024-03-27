// CREATE AN ORDER
document.getElementById("createFormID").addEventListener("submit", addOrder);

function addOrder(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let productID = document.getElementById("add_order_product_id").value;
	let customerID = document.getElementById("add_order_customer_id").value;
	let orderDate = document.getElementById("add_order_date").value;
	let orderQuantity = document.getElementById("add_order_quantity").value;
	// Validate input
	if (!validateInput(productID, customerID, orderDate, orderQuantity)) {
		return; // End script early if it returns false
	}

	let url = "/v2/order/add"; // API route
	let method = "POST"; // Method
	// Data
	let data = {
		product_id: productID,
		customer_id: customerID,
		order_date: orderDate,
		order_quantity: orderQuantity,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// UPDATE ORDER
document.getElementById("updateFormID").addEventListener("submit", updateOrder);

function updateOrder(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let orderID = document.getElementById("update_order_by_id").value;
	let orderField = document.getElementById("update_order_field").value;
	let newValue = document.getElementById("update_order_new_field").value;

	if (!validateInput(orderID, orderField, newValue)) {
		return;
	}

	let url = `/v2/order/update/${orderID}/${orderField}`;
	let method = "PUT";
	let data = {
		[orderField]: newValue,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// GET ORDER BY ID
document.getElementById("getFormID").addEventListener("submit", getOrderById);

function getOrderById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let orderID = document.getElementById("get_order_by_id").value;

	if (!validateInput(orderID)) {
		return;
	}

	let url = `/v2/order/get/${orderID}`;
	let method = "GET";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE ORDER
document.getElementById("deleteFormID").addEventListener("submit", deleteOrder);

function deleteOrder(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let orderID = document.getElementById("delete_order_by_id").value;

	if (!validateInput(orderID)) {
		return;
	}

	let url = `/v2/order/delete/${orderID}`;
	let method = "DELETE";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL ORDERS
document.getElementById("getAll").addEventListener("click", getAllOrders);

function getAllOrders() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/order/all";
	let method = "GET";
	prepareAndSendRequest(method, url);
}

//
//
//

// GET ORDER COUNT
document.getElementById("getCount").addEventListener("click", getOrderCount);

function getOrderCount() {
	document.getElementById("loading").style.display = "block";

	let count = true;
	let url = "/v2/order/count";
	let method = "GET";

	prepareAndSendRequest(method, url, count);
}

//
//
//

// Table headers
const columnHeaders = [
	"Order ID",
	"Product ID",
	"Customer ID",
	"Order Date",
	"Order Quantity",
];

function clearFields() {
	const allFields = [
		"add_order_product_id",
		"add_order_customer_id",
		"add_order_date",
		"add_order_quantity",
		"update_order_by_id",
		"update_order_field",
		"update_order_new_field",
		"get_order_by_id",
		"delete_order_by_id",
	];

	for (let field of allFields) {
		document.getElementById(field).value = "";
	}
}
