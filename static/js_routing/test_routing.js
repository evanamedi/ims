// ADD SUPPLIER
//--------------------------------------------------
document.getElementById("add-supplier").addEventListener("submit", addSupplier);
// EXECUTE
function addSupplier(event) {
	event.preventDefault();

	// Loading bar
	document.getElementById("loading").style.display = "block";

	// Get value of the input fields
	let supplierName = document.getElementById("supplier_name").value;
	let supplierAddress = document.getElementById("supplier_address").value;
	let supplierContact = document.getElementById("supplier_contact").value;

	// Input Validation
	if (!supplierName || !supplierAddress || !supplierContact) {
		alert("Please fill in all required fields");
		return;
	}

	// Prepare Data to be sent
	let url = "/v2/supplier/add";
	let data = {
		supplier_name: supplierName,
		supplier_address: supplierAddress,
		supplier_contact: supplierContact,
	};

	// Define options for the fetch request
	let options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
	};

	if (sendRequest(url, options)) {
		alert("Supplier Added Successfully");
	} else {
		alert("Failed To Add Supplier");
	}
}

// GET ALL SUPPLIERS
//--------------------------------------------------
document
	.getElementById("get-all-suppliers")
	.addEventListener("click", getAllSuppliers);
// EXECUTE
function getAllSuppliers() {
	// Loading bar
	document.getElementById("loading").style.display = "block";
	// Prepare request
	let url = "/v2/supplier/all";
	let options = {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	};

	if (!sendRequest(url, options)) {
		alert("Failed To Retrieve Supplier");
	}
}

// GET SUPPLIER COUNT
//--------------------------------------------------
document
	.getElementById("get-supplier-count")
	.addEventListener("click", getSupplierCount);
// EXECUTE
function getSupplierCount() {
	// Loading bar
	document.getElementById("loading").style.display = "block";
	// Prepare request
	let url = "/v2/supplier/count";
	let options = {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	};

	if (!sendRequestCount(url, options)) {
		alert("Failed To Retrieve Supplier Count");
	}
}

// UPDATE SUPPLIER
//--------------------------------------------------
document
	.getElementById("update-supplier-field")
	.addEventListener("submit", updateSupplier);
// EXECUTE
function updateSupplier(event) {
	event.preventDefault();

	// Loading bar
	document.getElementById("loading").style.display = "block";

	// Get value of the input fields
	let supplierID = document.getElementById("update-id").value;
	let field = document.getElementById("field").value;
	let newValue = document.getElementById("new-value").value;

	// Input Validation
	if (!supplierID || !field || !newValue) {
		alert("Please fill in all required fields");
		return;
	}

	// Prepare data to be sent
	let url = `/v2/supplier/update/${supplierID}/${field}`;
	let data = {
		[field]: newValue,
	};

	// Define options for the fetch request
	let options = {
		method: "PUT",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
	};

	if (sendRequest(url, options)) {
		alert("Supplier Updated Successfully");
	} else {
		alert("Failed To Update Supplier");
	}
}

// GET SUPPLIER BY ID
//--------------------------------------------------
document
	.getElementById("get-supplier-by-id")
	.addEventListener("submit", getSupplierById);
// EXECUTE
function getSupplierById(event) {
	event.preventDefault();

	// Loading bar
	document.getElementById("loading").style.display = "block";

	// Get value of the input fields
	let supplierID = document.getElementById("get-supplier-id").value;

	// Input Validation
	if (!supplierID) {
		alert("Please fill in all required fields");
		return;
	}

	// Prepare data to be sent
	let url = `/v2/supplier/get/${supplierID}`;
	let options = {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	};
	if (!sendRequest(url, options)) {
		alert("Failed To Retrieve Supplier");
	}
}

// DELETE SUPPLIER
//--------------------------------------------------
document
	.getElementById("delete-supplier")
	.addEventListener("submit", deleteSupplier);
//
function deleteSupplier(event) {
	event.preventDefault();

	// Loading bar
	document.getElementById("loading").style.display = "block";

	// Get value of the input fields
	let supplierID = document.getElementById("delete-supplier-id").value;

	// Input Validation
	if (!supplierID) {
		alert("Please fill in all required fields");
		return;
	}

	// Prepare data to be sent
	let url = `/v2/supplier/delete/${supplierID}`;
	let options = {
		method: "DELETE",
		headers: {
			"Content-Type": "application/json",
		},
	};

	if (sendRequest(url, options)) {
		alert("Supplier Deleted Successfully");
	} else {
		alert("Failed To Delete Supplier");
	}
}

function sendRequest(url, options) {
	// Send the request to the server
	fetch(url, options)
		.then((response) => {
			// Hide loading bar
			document.getElementById("loading").style.display = "none";
			// If the request was not successful, throw an error
			if (!response.ok) {
				// If the request was successful, parse the response body as JSON
				throw new Error(`HTTP Error- Status: ${response.status}`);
			}
			return response.json();
		})
		// Log the response data to the console
		.then((data) => {
			console.log(data);
			if (data.data[0] !== null)
				// Display response in element with id 'response'
				document.getElementById("response").innerHTML = generateHTML(
					data.data
				);
			// Clear input fields
			document.getElementById("supplier_name").value = "";
			document.getElementById("supplier_address").value = "";
			document.getElementById("supplier_contact").value = "";
			// Display success
		})

		.catch((error) => {
			// If there was an error with the fetch operation, log error message to console
			console.log(
				"There was a problem with fetch operation: " + error.message
			);
			// Display errors to the user
			document.getElementById("error").textContent =
				"There was a problem with the fetch operation: " +
				error.message;
			// Display Failure
			return false;
		});

	const columnHeaders = [
		"Supplier ID",
		"Supplier Name",
		"Supplier Address",
		"Supplier Contact",
	];
	// Function to display received data in HTML- takes an array of data objects as arg
	function generateHTML(dataArray) {
		let html = "<table class='h-fit'>"; // Create opening <table> tag
		html += "<tr>"; // Generate table header
		for (let header of columnHeaders) {
			html += `<th class="tableHeader">${header}</th>`;
		}
		html += `<tr><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td></tr>`;
		html += `<tr><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td></tr>`;
		html += "</tr>";
		for (let data of dataArray) {
			// Loop over each data array in dataArray
			html += "<tr>"; // Add opening tag for table row
			for (let i = 0; i < columnHeaders.length; i++) {
				// Loop through each column index
				html += `<td class="row">${data[i]}</td>`; // Add table cell with value of current index
			}
			html += "</tr>"; // Closing tag for table row
			html += `<tr><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td></tr>`;
		}
		html += "</table>"; // Closing tag for table
		return html; // Return HTML string
	}
	return true;
}

function sendRequestCount(url, options) {
	// Send the request to the server
	fetch(url, options)
		.then((response) => {
			// Hide loading bar
			document.getElementById("loading").style.display = "none";
			// If the request was not successful, throw an error
			if (!response.ok) {
				// If the request was successful, parse the response body as JSON
				throw new Error(`HTTP Error- Status: ${response.status}`);
			}
			return response.json();
		})
		// Log the response data to the console
		.then((data) => {
			console.log(data);
			if (data.data[0] !== null)
				// Display response in element with id 'response'
				document.getElementById("response").innerHTML = generateHTML(
					data.data
				);
			// Clear input fields
			document.getElementById("supplier_name").value = "";
			document.getElementById("supplier_address").value = "";
			document.getElementById("supplier_contact").value = "";
			// Display success
		})

		.catch((error) => {
			// If there was an error with the fetch operation, log error message to console
			console.log(
				"There was a problem with fetch operation: " + error.message
			);
			// Display errors to the user
			document.getElementById("error").textContent =
				"There was a problem with the fetch operation: " +
				error.message;
			// Display Failure
			return false;
		});

	// Function to display received data in HTML- takes an array of data objects as arg
	function generateHTML(data) {
		let html = `<div>Count: ${data[0]}</div>`;
		return html;
		// Return HTML string
	}
	return true;
}

document.getElementById("clear").addEventListener("click", clearDisplay);

function clearDisplay() {
	document.getElementById("response").innerHTML = "";
}
