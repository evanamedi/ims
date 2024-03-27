// CREATE A SALE
document.getElementById("createFormID").addEventListener("submit", addSale);

function addSale(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input fields
	let productID = document.getElementById("add_sale_product_id").value;
	let customerID = document.getElementById("add_sale_customer_id").value;
	let saleDate = document.getElementById("add_sale_date").value;
	let saleQuantity = document.getElementById("add_sale_quantity").value;
	// Validate input
	if (!validateInput(productID, customerID, saleDate, saleQuantity)) {
		return; // End script early if it returns false
	}

	let url = "/v2/sale/add"; // API route
	let method = "POST"; // Method
	// Data
	let data = {
		product_id: productID,
		customer_id: customerID,
		sale_date: saleDate,
		sale_quantity: saleQuantity,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// UPDATE SALE
document.getElementById("updateFormID").addEventListener("submit", updateSale);

function updateSale(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let saleID = document.getElementById("update_sale_by_id").value;
	let saleField = document.getElementById("update_sale_field").value;
	let newValue = document.getElementById("update_sale_new_field").value;

	if (!validateInput(saleID, saleField, newValue)) {
		return;
	}

	let url = `/v2/sale/update/${saleID}/${saleField}`;
	let method = "PUT";
	let data = {
		[saleField]: newValue,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// GET SALE BY ID
document.getElementById("getFormID").addEventListener("submit", getSaleById);

function getSaleById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let saleID = document.getElementById("get_sale_by_id").value;

	if (!validateInput(saleID)) {
		return;
	}

	let url = `/v2/sale/get/${saleID}`;
	let method = "GET";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE SALE
document.getElementById("deleteFormID").addEventListener("submit", deleteSale);

function deleteSale(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let saleID = document.getElementById("delete_sale_by_id").value;

	if (!validateInput(saleID)) {
		return;
	}

	let url = `/v2/sale/delete/${saleID}`;
	let method = "DELETE";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL SALES
document.getElementById("getAll").addEventListener("click", getAllSales);

function getAllSales() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/sale/all";
	let method = "GET";
	prepareAndSendRequest(method, url);
}

//
//
//

// GET SALE COUNT
document.getElementById("getCount").addEventListener("click", getSaleCount);

function getSaleCount() {
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
	"Sale ID",
	"Product ID",
	"Customer ID",
	"Sale Data",
	"Sale Quantity",
];

function clearFields() {
	const allFields = [
		"add_sale_product_id",
		"add_sale_customer_id",
		"add_sale_date",
		"add_sale_quantity",
		"update_sale_by_id",
		"update_sale_field",
		"update_sale_new_field",
		"get_sale_by_id",
		"delete_sale_by_id",
	];

	for (let field of allFields) {
		document.getElementById(field).value = "";
	}
}
