// GLOBAL FUNCTIONS
//
//
//

// For sending data
function prepareAndSendData(method, data, url) {
	let options = {
		method: method,
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
	};

	sendRequest(url, options);

	// if (sendRequest(url, options)) {
	// 	alert("Request Completed Successfully");
	// } else {
	// 	alert("Request Failed");
	// }
}

//
//
//

// For requesting data or sending actions
function prepareAndSendRequest(method, url, count) {
	let options = {
		method: method,
		headers: {
			"Content-Type": "application/json",
		},
	};

	sendRequest(url, options, count);

	// if (!sendRequest(url, options, count)) {
	// 	alert("Request Failed");
	// }
}

//
//
//

// For validating that all input fields are filled
function validateInput(...args) {
	if (args.some((arg) => !arg)) {
		alert("Please fill in all required fields");
		return false; // Return false if at least one element is empty
	}
	return true; // Return true otherwise
}

//
//
//

// For clearing all data/fields
document.getElementById("clear").addEventListener("click", clearDisplay);
function clearDisplay() {
	document.getElementById("response").innerHTML = "";
}

//
//
//

// Function for sending requests
function sendRequest(url, options, count) {
	// Send the request to the server
	fetch(url, options)
		.then((response) => {
			// Hide loading bar
			document.getElementById("loading").style.display = "none";
			// If the request was not successful, throw an error
			if (!response.ok) {
				throw new Error(`HTTP Error- Status: ${response.status}`);
			}
			// If the request was successful, parse the response body as JSON
			return response.json();
		})

		// Log the response data to the console
		.then((data) => {
			console.log(data);
			if (data.data[0] !== null) {
				// Display response in element with id 'response'
				document.getElementById("response").innerHTML = generateHTML(
					data.data,
					count
				);
			}
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
		});
}

//
//
//

// Function to display received data in HTML- takes an array of data objects as arg
function generateHTML(dataArray, count) {
	if (count) {
		// Function to display received data in HTML- takes an array of data objects as arg
		let html = `<div>Count: ${dataArray[0][0]}</div>`;
		return html;
		// Return HTML string
	} else {
		let html = "<table class='h-fit'>"; // Create opening <table> tag
		html += "<tr>"; // Generate table header
		for (let header of columnHeaders) {
			html += `<th>${header}</th>`;
		}

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
}

// html += `<tr class="blankRow"></tr>`;
// html += `<tr class="blankRow"></tr>`;
