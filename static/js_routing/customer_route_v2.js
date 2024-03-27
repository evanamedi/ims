// CREATE A CUSTOMER
document.getElementById("createFormID").addEventListener("submit", addCustomer);

function addCustomer(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let customerName = document.getElementById("add_customer_name").value;
	let customerAddress = document.getElementById("add_customer_contact").value;
	let customerContact = document.getElementById("add_customer_contact").value;
	// Validate input
	if (!validateInput(customerName, customerAddress, customerContact)) {
		return; // End script early if it returns false
	}

	let url = "/v2/customer/add"; // API route
	let method = "POST"; // Method
	// Data
	let data = {
		customer_name: customerName,
		customer_address: customerAddress,
		customer_contact: customerContact,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// UPDATE CUSTOMER
document
	.getElementById("updateFormID")
	.addEventListener("submit", updateCustomer);

function updateCustomer(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let customerID = document.getElementById("update_customer_by_id").value;
	let customerField = document.getElementById("update_customer_field").value;
	let newValue = document.getElementById("update_customer_new_field").value;

	if (!validateInput(customerID, customerField, newValue)) {
		return;
	}

	let url = `/v2/customer/update/${customerID}/${customerField}`;
	let method = "PUT";
	let data = {
		[customerField]: newValue,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// GET CUSTOMER BY ID
document
	.getElementById("getFormID")
	.addEventListener("submit", getCustomerById);

function getCustomerById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let customerID = document.getElementById("get_customer_by_id").value;

	if (!validateInput(customerID)) {
		return;
	}

	let url = `/v2/customer/get/${customerID}`;
	let method = "GET";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE CUSTOMER
document
	.getElementById("deleteFormID")
	.addEventListener("submit", deleteCustomer);

function deleteCustomer(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let customerID = document.getElementById("delete_customer_by_id").value;

	if (!validateInput(customerID)) {
		return;
	}

	let url = `/v2/customer/delete/${customerID}`;
	let method = "DELETE";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL CUSTOMERS
document.getElementById("getAll").addEventListener("click", getAllCustomers);

function getAllCustomers() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/customer/all";
	let method = "GET";
	prepareAndSendRequest(method, url);
}

//
//
//

// GET CUSTOMER COUNT
document.getElementById("getCount").addEventListener("click", getCustomerCount);

function getCustomerCount() {
	document.getElementById("loading").style.display = "block";

	let count = true;
	let url = "/v2/customer/count";
	let method = "GET";

	prepareAndSendRequest(method, url, count);
}

//
//
//

// Table headers
const columnHeaders = [
	"Customer ID",
	"Customer Name",
	"Customer Address",
	"Customer Contact",
];

function clearFields() {
	const allFields = [
		"add_customer_name",
		"add_customer_address",
		"add_customer_contact",
		"update_customer_by_id",
		"update_customer_field",
		"update_customer_new_field",
		"get_customer_by_id",
		"delete_customer_by_id",
	];

	for (let field of allFields) {
		document.getElementById(field).value = "";
	}
}
