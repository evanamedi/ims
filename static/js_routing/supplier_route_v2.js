/* Currently have the supplier, client-side routing, implemented and working
however i don't want to repeat this code with the other pages
so were doing to decouple them here, and break the logic into
functions that can accept data from any of the pages */

// ADD SUPPLIER
document.getElementById("add-supplier").addEventListener("submit", addSupplier);

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
	.getElementById("update-supplier-field")
	.addEventListener("submit", updateSupplier);

function updateSupplier(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let supplier_id = document.getElementById("update-id").value;
	let field = document.getElementById("field").value;
	let newValue = document.getElementById("new-value").value;
	// Validate input
	if (!validateInput(supplier_id, field, newValue)) {
		return; // If it returns false, script will end early
	}

	let url = `/v2/supplier/update/${supplier_id}/${field}`; // API route
	let method = "PUT"; // Method
	// Data
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
	.getElementById("get-supplier-by-id")
	.addEventListener("submit", getSupplierById);

function getSupplierById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let supplier_id = document.getElementById("get-supplier-id").value;
	// Validate input
	if (!validateInput(supplier_id)) {
		return; // If it returns false, script will end early
	}

	let url = `/v2/supplier/get/${supplier_id}`; // API route
	let method = "GET"; // Method

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// DELETE SUPPLIER
document
	.getElementById("delete-supplier")
	.addEventListener("submit", deleteSupplier);

function deleteSupplier(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// Get input data
	let supplier_id = document.getElementById("delete-supplier-id").value;
	// Validate input
	if (!validateInput(supplier_id)) {
		return; // If it returns false, script will end early
	}

	let url = `/v2/supplier/delete/${supplier_id}`; // API route
	let method = "DELETE"; // Method

	prepareAndSendRequest(method, url);
	clearFields();
}

//
//
//

// GET ALL SUPPLIERS
document
	.getElementById("get-all-suppliers")
	.addEventListener("click", getAllSuppliers);

function getAllSuppliers() {
	document.getElementById("loading").style.display = "block";

	let url = "/v2/supplier/all"; // API route
	let method = "GET"; // Method

	prepareAndSendRequest(method, url);
}

//
//
//

// GET SUPPLIER COUNT
document
	.getElementById("get-supplier-count")
	.addEventListener("click", getSupplierCount);

function getSupplierCount() {
	document.getElementById("loading").style.display = "block";

	let count = true;
	let url = "/v2/supplier/count"; // API route
	let method = "GET"; // Method

	prepareAndSendRequest(method, url, count);
}

//
//
//

const columnHeaders = [
	"Supplier ID",
	"Supplier Name",
	"Supplier Address",
	"Supplier Contact",
];

// Clear input fields
function clearFields() {
	document.getElementById("supplier_name").value = "";
	document.getElementById("supplier_address").value = "";
	document.getElementById("supplier_contact").value = "";
	document.getElementById("update-id").value = "";
	document.getElementById("field").value = "";
	document.getElementById("new-value").value = "";
	document.getElementById("get-supplier-id").value = "";
	document.getElementById("delete-supplier-id").value = "";
}
