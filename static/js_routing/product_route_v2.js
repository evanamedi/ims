// sup homie hows your day goin?
// this is gonna be the client-side routing for adding a new product, cool?
document.getElementById("createFormID").addEventListener("submit", addProduct);

function addProduct(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let supplierID = document.getElementById("add_product_supplier_id").value;
	let productName = document.getElementById("add_product_name").value;
	let productDescription = document.getElementById(
		"add_product_description"
	).value;
	let productPrice = document.getElementById("add_product_price").value;
	let productQuantity = document.getElementById("add_product_quantity").value;
	// Validate input
	if (
		!validateInput(
			supplierID,
			productName,
			productDescription,
			productPrice,
			productQuantity
		)
	) {
		return; // If it returns false, script will end early
	}

	let url = "/v2/product/add"; // API route
	let method = "POST"; // Method
	// Data
	let data = {
		supplier_id: supplierID,
		product_name: productName,
		product_description: productDescription,
		product_price: productPrice,
		product_quantity: productQuantity,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// UPDATE PRODUCT
document
	.getElementById("updateFormID")
	.addEventListener("submit", updateProduct);

function updateProduct(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let productID = document.getElementById("update_product_by_id").value;
	let productField = document.getElementById("update_product_field").value;
	let newValue = document.getElementById("update_product_new_field").value;

	if (!validateInput(productID, productField, newValue)) {
		return;
	}

	let url = `/v2/product/update/${productID}/${productField}`;
	let method = "PUT";
	let data = {
		[field]: newValue,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// GET PRODUCT BY ID
document.getElementById("getFormID").addEventListener("submit", getProductById);

function getProductById(event) {
	event.preventDefault("loading").style.display = "block";
	document.getElementById("loading").style.display = "block";

	let productID = document.getElementById("get_product_by_id").value;

	if (!validateInput(productID)) {
		return;
	}

	let url = `/v2/product/get/${productID}`;
	let method = "GET";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE PRODUCT
document
	.getElementById("deleteFormID")
	.addEventListener("submit", deleteProduct);

function deleteProduct(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let productID = document.getElementById("delete_product_by_id");

	if (!validateInput(productID)) {
		return;
	}

	let url = `/v2/product/delete/${productID}`;
	let method = "DELETE";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL PRODUCTS
document.getElementById("getAll").addEventListener("click", getAllProducts);

function getAllProducts() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/product/all";
	let method = "GET";
	prepareAndSendRequest(method, url);
}

//
//
//

// GET PRODUCT COUNT

document.getElementById("getCount").addEventListener("click", getProductCount);

function getProductCount() {
	document.getElementById("loading").style.display = "block";

	let count = true;
	let url = "/v2/product/count";
	let method = "GET";

	prepareAndSendRequest(method, url, count);
}

// DISPLAY TABLE HEADERS
const columnHeaders = [
	"Product ID",
	"Supplier ID",
	"Product Name",
	"Description",
	"Price",
	"Quantity",
];

function clearFields() {
	const allFields = [
		"add_product_supplier_id",
		"add_product_name",
		"add_product_description",
		"add_product_price",
		"add_product_quantity",
		"update_product_by_id",
		"update_product_new_field",
		"update_product_new_field",
		"get_product_by_id",
		"delete_product_by_id",
	];

	for (let field of allFields) {
		document.getElementById(field).value = "";
	}
}
