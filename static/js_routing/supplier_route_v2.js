/* Currently have the supplier, client-side routing, implemented and working
however i don't want to repeat this code with the other pages
so were doing to decouple them here, and break the logic into
functions that can accept data from any of the pages */

// GET ALL PRODUCTS AND DROP DOWN SELECTIONS
window.onload = function () {
	getAllSuppliers();
	dropDownOptions();
};

// GENERATE OPTIONS FOR DROP DOWN MENU
function dropDownOptions() {
	supplierData = JSON.parse(sessionStorage.getItem("suppliers"));
	document.getElementById("update-id").innerHTML = selectMenu(
		supplierData.data
	);
	document.getElementById("get-supplier-id").innerHTML = selectMenu(
		supplierData.data
	);
	document.getElementById("delete-supplier-id").innerHTML = selectMenu(
		supplierData.data
	);
}

// ADD SUPPLIER
document.getElementById("createFormID").addEventListener("submit", addSupplier);

function addSupplier(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let supplierName = document.getElementById("supplier_name").value;
	let supplierAddress = document.getElementById("supplier_address").value;
	let supplierContact = document.getElementById("supplier_contact").value;
	// Validate input
	if (!validateInput(supplierName, supplierAddress, supplierContact)) {
		return; // If it returns false, script will end early
	}

	let url = "/v2/supplier/add"; // API route
	let method = "POST"; // Method
	// Data
	let data = {
		supplier_name: supplierName,
		supplier_address: supplierAddress,
		supplier_contact: supplierContact,
	};

	prepareAndSendData(method, data, url);
	clearFields();
}

//
//
//

// UPDATE SUPPLIER
document
	.getElementById("updateFormID")
	.addEventListener("submit", updateSupplier);

function updateSupplier(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let supplier_id = document.getElementById("update-id").value;
	let field = document.getElementById("field").value;
	let newValue = document.getElementById("new-value").value;

	if (!validateInput(supplier_id, field, newValue)) {
		return;
	}

	let url = `/v2/supplier/update/${supplier_id}/${field}`;
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

// GET SUPPLIER BY ID
document
	.getElementById("getFormID")
	.addEventListener("submit", getSupplierById);

function getSupplierById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let supplier_id = document.getElementById("get-supplier-id").value;

	if (!validateInput(supplier_id)) {
		return;
	}

	let url = `/v2/supplier/get/${supplier_id}`;
	let method = "GET";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE SUPPLIER
document
	.getElementById("deleteFormID")
	.addEventListener("submit", deleteSupplier);

function deleteSupplier(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let supplier_id = document.getElementById("delete-supplier-id").value;

	if (!validateInput(supplier_id)) {
		return;
	}

	let url = `/v2/supplier/delete/${supplier_id}`;
	let method = "DELETE";

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL SUPPLIERS
function getAllSuppliers() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/supplier/all";
	let method = "GET";

	prepareAndSendRequest(method, url);
}

//
//
//

// DISPLAY ALL SUPPLIERS
document
	.getElementById("getAll")
	.addEventListener("click", displayAllSuppliers);
function displayAllSuppliers() {
	data = JSON.parse(sessionStorage.getItem("suppliers"));
	document.getElementById("response").innerHTML = generateHTML(data.data);
	console.log(data.message[0]);
}

//
//
//

// DISPLAY SUPPLIER COUNT
document.getElementById("getCount").addEventListener("click", getSupplierCount);

function getSupplierCount() {
	let data = JSON.parse(sessionStorage.getItem("suppliers"));
	document.getElementById("response").innerHTML = generateHTML(
		data.data.length,
		true
	);
}

//
//
//

// DISPLAY TABLE HEADERS
const columnHeaders = [
	"Supplier ID",
	"Supplier Name",
	"Supplier Address",
	"Supplier Contact",
];

function clearFields() {
	const allFields = [
		"supplier_name",
		"supplier_address",
		"supplier_contact",
		"update-id",
		"field",
		"new-value",
		"get-supplier-id",
		"delete-supplier-id",
	];
	for (let field of allFields) {
		document.getElementById(field).value = "";
	}
}
