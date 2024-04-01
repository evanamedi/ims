// Base URL for all API routes
const BASE_URL = "/v2/supplier";

// Handle responses
function handleResponse(response) {
	if (!response.ok) {
		throw Error(response.statusText);
	}
	return response.json();
}

// Handle errors
function handleError(error) {
	console.error("An error occurred:", error);
	// Display message
	document.getElementById("message").textContent = error.message;
}

// Display Data
function displayData(response) {
	// Clear any data
	const output = document.getElementById("output");
	output.innerHTML = "";

	// Check if data is array (if multiple lines are being returned)
	if (Array.isArray(response.data)) {
		response.data.forEach((supplier) => {
			if (supplier !== null) {
				const supplierDiv = document.createElement("div");
				supplierDiv.textContent = `ID: ${supplier[0]}, Name: ${supplier[1]}, Address: ${supplier[2]}, Contact: ${supplier[3]}`;
				output.appendChild(supplierDiv);
			}
		});
	} else {
		// Single
		if (response.data !== null) {
			const supplierDiv = document.createElement("div");
			supplierDiv.textContent = `ID: ${response.data[0]}, Name: ${response.data[1]}, Address: ${response.data[2]}, Contact: ${response.data[3]}`;
			output.appendChild(supplierDiv);
		}
	}
}

// Make a request
function makeRequest(method, endpoint, data) {
	const url = `${BASE_URL}${endpoint}`;
	const options = {
		method: method,
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
	};

	fetch(url, options)
		.then(handleResponse)
		.then(displayData)
		.catch(handleError);
}

// Get all suppliers
document
	.getElementById("get-all-suppliers")
	.addEventListener("click", function () {
		makeRequest("GET", "/all");
	});

// Get supplier count
document
	.getElementById("get-supplier-count")
	.addEventListener("click", function () {
		makeRequest("GET", "/count");
	});

// Add a supplier
document
	.getElementById("add-supplier")
	.addEventListener("submit", function (event) {
		event.preventDefault();
		const data = {
			supplier_name: document.getElementById("name").value,
			supplier_address: document.getElementById("address").value,
			supplier_contact: document.getElementById("contact").value,
		};
		makeRequest("POST", "/add", data);
	});

// Update a supplier
document
	.getElementById("update-supplier-field")
	.addEventListener("submit", function (event) {
		event.preventDefault();
		const supplierId = document.getElementById("update-id").value;
		const field = document.getElementById("field").value;
		const newValue = document.getElementById("new-value").value;
		const data = { [field]: newValue };
		makeRequest("PUT", `update/${supplierId}`, data);
	});

// Get Supplier by ID
document
	.getElementById("get-supplier-by-id")
	.addEventListener("submit", function (event) {
		event.preventDefault();
		const supplierId = document.getElementById("get-supplier-id").value;
		makeRequest("GET", `/${supplierId}`);
	});

// Delete a supplier
document
	.getElementById("delete-supplier")
	.addEventListener("submit", function (event) {
		event.preventDefault();
		const supplierId = document.getElementById("delete-supplier-id").value;
		makeRequest("DELETE", `delete/${supplierId}`);
	});
