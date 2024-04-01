// ---------- DISPLAY COUNT SWITCH ----------
/**
This is turned off by default. It gets turned on when getCount is triggered, 
then turned off again once its used in generateHTML()
 */
let table = document.getElementById("pageName").value;

// ---------- PREP DATA TO BE SENT ----------
/** 
This function prepares and packages its method, 
and data if it contains any
*/
function prepareAndSend(method, url, data) {
	let options = {
		method: method,
		headers: {
			"Content-Type": "application/json",
		},
	};
	if (data) {
		options["body"] = JSON.stringify(data);
		console.log(options);
	}

	sendRequest(url, options);
}

// ---------- VALIDATE INPUT ----------
/**
For validating that all input fields are filled,
will need to add more robust checking in the future
It will return false if at least one element is empty
Return true otherwise
 */

function validateInput(...args) {
	if (args.some((arg) => !arg)) {
		alert("Please fill in all required fields");
		return false;
	}
	return true;
}

// ---------- CLEAR TABLE (manual) ----------
/**
For clearing the response display (tables)- executed on click
 */
document.getElementById("clear").addEventListener("click", clearDisplay);
function clearDisplay() {
	document.getElementById("response").innerHTML = "";
}

// ---------- PROMISE ME A SUCCESS ----------
/**
// Function for sending requests
 */
function sendRequest(url, options) {
	fetch(url, options) // Send the request to the server
		.then((response) => {
			if (!response.ok) {
				throw new Error(`HTTP Error- Status: ${response.status}`); // If the request was not successful, throw an error
			}
			return response.json(); // If the request was successful, parse the response body as JSON
		})
		.then((data) => {
			console.log(data);
			console.log(data.data);
			console.log(data.table); // Log the response message to the console
			// If there was data returned, store it in session storage to use
			if (data.data[0] !== null) {
				sessionStorage.setItem(
					`${table}`,
					JSON.stringify(data.data)
				);
			}
		})
		.catch((error) => {
			console.log(
				"There was a problem with fetch operation: " +
					error.message
			); // If there was an error with the fetch operation, log error message to console
			document.getElementById("error").textContent =
				"There was a problem with the fetch operation: " +
				error.message; // Display errors to the user
		});
	document.getElementById("loading").classList.add("hidden"); // Hide loading bar
}

// ---------- GENERATE HTML ----------
/**
Parse data into HTML
 */
function generateHTML(dataArray, count) {
	const blank = `<tr><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td><td class="blankRow"></td></tr>`;
	if (count) {
		count = false; // Turn off count switch
		let html = `<div>Count: ${dataArray}</div>`; // Generate HTML string
		return html; // Return HTML string
	} else {
		// TABLE HEADERS
		let html = "<table class='h-fit'>"; // Create opening <table> tag
		html += `<tr >`; // Generate table row
		headers = tableHeadersMapping[table];
		for (let header of headers) {
			html += `<th class='header'>${header}</th>`; // Generate all column headers
		}
		html += "</tr>";
		html += blank + blank + blank + blank;
		// TABLE ROWS

		for (let data of dataArray) {
			// Loop over each array in dataArray
			html += `<tr>`; // Add opening tag for new table row
			for (let i = 0; i < tableHeadersMapping[table].length; i++) {
				// Loop through each column index
				html += `<td class="row">${Object.values(data)[i]}</td>`; // Add table cell with value of current index
			}
			html += "</tr>"; // Closing tag for table row
			html += blank;
		}
		html += "</table>"; // Closing tag for table
		return html; // Return HTML string
	}
}

//
//
//
//
//
//
//
//
//
//
// OLD JAZZ
//
//
//
//
//
// // ---------- CLEAR INPUT FIELDS (auto) ----------
// /**
// ya know clear all input fields- executed after functions
//
// function clearAllForms() {
// 	var forms = document.getElementsByTagName("form");

// 	Array.form(forms).forEach(function (form) {
// 		form.reset();
// 	});
// }
//
//  */

// ---------- PARSE DROPDOWN DATA ----------
/**
Taking the pageList array, and data stored in sessionStorage, 
this function organizes the data needed for each dropdown menu
It first does the default ids that each pages has,
then if there are other items present, it will parse those as well
**NOTE**
Not crazy about this current implementation, 
may have this data parsed server-side in the future
 */

// function getDropDownData() {
// 	pageData = JSON.parse(sessionStorage.getItem(`${pageList[0]}`));
// 	const pageDropDown = ["update_id", "get_id", "delete_id"];
// 	for (let ID of pageDropDown) {
// 		document.getElementById(ID).innerHTML = selectMenu(pageData);
// 	}

// 	for (let i = 1; i < pageList.length; i++) {
// 		otherData = JSON.parse(sessionStorage.getItem(`${pageList[i]}`));
// 		document.getElementById(
// 			`add_${pageList[0]}_${pageList[i]}_id`
// 		).innerHTML = selectMenu(otherData.data);
// 	}
// }

// // ---------- GENERATE DROP DOWN CONTENT OPTIONS ----------
// /**
// For all of the input fields that required data already in the database,
// this function will generate a menu that the user can use to select the
// data they want to manipulate
//  */
// function selectMenu(selectionData) {
// 	let htmlOption = `<option></option>`;
// 	for (let data of selectionData) {
// 		htmlOption += `<option>${data.id}</option>`;
// 	}
// 	console.log(htmlOption);
// 	return htmlOption;
// }
