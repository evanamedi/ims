// Using Supplier API for Testing

let supplierName = document.getElementById("supplier_anem").value;
let supplierAddress = document.getElementById("supplier_address").value;
let supplierContact = document.getElementById("supplier_contact").value;

let url = "/v2/supplier/add";
let data = {
	supplier_name: supplierName,
	supplier_address: supplierAddress,
	supplier_contact: supplierContact,
};

let options = {
	method: "POST",
	headers: {
		"Content-Type": "application/json",
	},
	body: JSON.stringify(data),
};

fetch(url, options)
	.then((response) => {
		if (!response.ok) {
			throw new Error(`HTTP Error- Status: ${response.status}`);
		}
		return response.json();
	})
	.then((data) => {
		console.log(data);
	})

	.catch((error) => {
		console.log(
			"There was a problem with fetch operation: " + error.message
		);
	});
