// ---------- ONLOAD TRIGGER ----------
/**
Trigger functions to get data, and populate dropdown menu
 */
window.onload = function () {
	getAll();
};

// ---------- GET ALL ----------
/**
This function will retrieve all the data for fields listed in the pageList array
 */
function getAll() {
	document.getElementById("loading").classList.toggle("hidden");
	let url = `/api/v3/${table}/query/all`;
	let method = "GET";
	prepareAndSend(method, url);
}

// ---------- CREATE ----------
/**
1) Initialize object to contain input-field data
2) Loop through each value in createObjectMapping, whos key is the first index of pageList
3) Get content of id that matches the current value of arrayElement
4) Validate element is not empty
5) Assign value (which was input) to its respective key, within the data object
6) Note that this is slicing off "add_" from the key to match what the api is expecting. Still unsure of this approach
7) Build url using first index of pageList
8) Send homie out for processing
 */
// Create new (x)
document
	.getElementById("createFormID")
	.addEventListener("submit", createObject);

function createObject(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	let data = {}; // 1
	// 2
	for (let arrayElement of createObjectMapping[table]) {
		let currentData = document.getElementById(`${arrayElement}`).value; // 3
		if (!validateInput(currentData)) {
			// 4
			return;
		}
		data[arrayElement] = currentData; // 5, 6
		console.log(data);
	}

	let url = `/api/v3/${table}/create`; // 7
	const method = "POST";
	console.log(data);
	prepareAndSend(method, url, data); // 8
}

// ---------- UPDATE ----------
/**
1) Get all input values from fields that match the id
2) Validate
3) Build url
 */
// Update (x)
document
	.getElementById("updateFormID")
	.addEventListener("submit", updateObject);

function updateObject(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";
	// 1
	let ID = document.getElementById("update_id").value;
	let field = document.getElementById("update_field").value;
	let newField = document.getElementById("update_new_field");

	if (!validateInput(ID, field, newField)) {
		return;
	}

	let url = `/api/v3/${table}/${ID}/`;
	let method = "PUT";
	let data = {
		[field]: newField.value,
	};

	prepareAndSend(method, url, data);
}

// ---------- GET BY ID ----------
/**
DOES NOT CURRENTLY HAVE METHOD TO DISPLAY DATA
 */
// by default uses: get_id
document
	.getElementById("getFormID")
	.addEventListener("submit", getObjectById);

function getObjectById(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let ID = document.getElementById("get_id").value;

	if (!validateInput(ID)) {
		return;
	}

	let url = `/api/v3/${table}/${ID}`;
	let method = "GET";

	prepareAndSend(method, url);
}

// ---------- DELETE BY ID ----------
/**
 *
 */
// by default uses: delete_id
document
	.getElementById("deleteFormID")
	.addEventListener("submit", deleteObject);

function deleteObject(event) {
	event.preventDefault();
	document.getElementById("loading").style.display = "block";

	let ID = document.getElementById("delete_id").value;

	if (!validateInput(ID)) {
		return;
	}

	let url = `/api/v3/${table}/${ID}`;
	let method = "DELETE";

	prepareAndSend(method, url);
}

// ---------- DISPLAY ALL ----------
/**
This will display the table, and populate the fields
 */
document.getElementById("getAll").addEventListener("click", displayAll);

function displayAll() {
	data = JSON.parse(sessionStorage.getItem(`${table}`));
	document.getElementById("response").innerHTML = generateHTML(data);
}

let count = false;
// ---------- DISPLAY COUNT ----------
/**
This is will get the row count for table
 */
document.getElementById("getCount").addEventListener("click", getCount);

function getCount() {
	let data = JSON.parse(sessionStorage.getItem(`${table}`));
	document.getElementById("response").innerHTML = generateHTML(
		Object.values(data).length,
		true
	);
}
