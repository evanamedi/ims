let createButton = document.getElementById("createButtonID");
let updateButton = document.getElementById("updateButtonID");
let getByIdButton = document.getElementById("getByIdButtonID");
let deleteButton = document.getElementById("deleteButtonID");

// ADD A NEW SUPPLIER
let createForm = document.getElementById("add-supplier");
// TOGGLE ON
createButton.addEventListener("click", function (event) {
	event.stopPropagation();
	createSupplier(true);
	deleteSupplier(false);
	getSupplier(false);
	updateSupplier(false);
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	if (!createForm.contains(event.target)) createSupplier(false);
});

//
//
//

// UPDATE SUPPLIER
let updateField = document.getElementById("update-supplier-field");
// TOGGLE ON
updateButton.addEventListener("click", function (event) {
	event.stopPropagation();
	updateSupplier(true);
	createSupplier(false);
	getSupplier(false);
	deleteSupplier(false);
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	if (!updateField.contains(event.target)) updateSupplier(false);
});

//
//
//

// GET SUPPLIER BY ID
let getFormID = document.getElementById("get-supplier-by-id");
// TOGGLE ON
getByIdButton.addEventListener("click", function (event) {
	event.stopPropagation();
	getSupplier(true);
	createSupplier(false);
	updateSupplier(false);
	deleteSupplier(false);
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	if (!getFormID.contains(event.target)) getSupplier(false);
});

//
//
//

// DELETE SUPPLIER
let deleteForm = document.getElementById("delete-supplier");
// TOGGLE ON
deleteButton.addEventListener("click", function (event) {
	event.stopPropagation();
	deleteSupplier(true);
	createSupplier(false);
	updateSupplier(false);
	getSupplier(false);
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	if (!deleteForm.contains(event.target)) deleteSupplier(false);
});

//
//
//
//
//
//
//
// FUNCTIONS
//
//

// CREATE SUPPLIER BUTTON FUNCTION
function createSupplier(bool) {
	if (bool) {
		return (
			createForm.classList.toggle("hidden"),
			createButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			createForm.classList.add("hidden"),
			createButton.classList.remove("toggleButton")
		);
	}
}
//
//
//
//
//
// UPDATE SUPPLIER BUTTON FUNCTION
function updateSupplier(bool) {
	if (bool) {
		return (
			updateField.classList.toggle("hidden"),
			updateButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			updateField.classList.add("hidden"),
			updateButton.classList.remove("toggleButton")
		);
	}
}

// GET SUPPLIER BUTTON FUNCTION
function getSupplier(bool) {
	if (bool) {
		return (
			getFormID.classList.toggle("hidden"),
			getByIdButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			getFormID.classList.add("hidden"),
			getByIdButton.classList.remove("toggleButton")
		);
	}
}

// DELETE SUPPLIER BUTTON FUNCTION
function deleteSupplier(bool) {
	if (bool) {
		return (
			deleteForm.classList.toggle("hidden"),
			deleteButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			deleteForm.classList.add("hidden"),
			deleteButton.classList.remove("toggleButton")
		);
	}
}
