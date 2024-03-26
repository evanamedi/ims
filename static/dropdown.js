// Table Page Selection
let selectionButton = document.getElementById("tableSelectButton");
let selectionMenu = document.getElementById("selectionMenu");

selectionButton.addEventListener("click", function (event) {
	event.stopPropagation();
	selectionMenu.classList.toggle("hidden");
});

window.addEventListener("click", function (event) {
	if (!selectionMenu.contains(event.target))
		selectionMenu.classList.add("hidden");
});

// CREATE SUPPLIER BUTTON
let createButton = document.getElementById("createID");
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

// UPDATE SUPPLIER BUTTON
let updateButton = document.getElementById("updateForm");
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

// GET SUPPLIER BUTTON
let getSupplierButton = document.getElementById("getSupplierID");
let getFormID = document.getElementById("get-supplier-by-id");
// TOGGLE ON
getSupplierButton.addEventListener("click", function (event) {
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

// DELETE SUPPLIER BUTTON
let deleteSupplierButton = document.getElementById("deleteSupplier");
let deleteForm = document.getElementById("delete-supplier");

deleteSupplierButton.addEventListener("click", function (event) {
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
// FUNCTIONS
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
			getSupplierButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			getFormID.classList.add("hidden"),
			getSupplierButton.classList.remove("toggleButton")
		);
	}
}

// DELETE SUPPLIER BUTTON FUNCTION
function deleteSupplier(bool) {
	if (bool) {
		return (
			deleteForm.classList.toggle("hidden"),
			deleteSupplierButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			deleteForm.classList.add("hidden"),
			deleteSupplierButton.classList.remove("toggleButton")
		);
	}
}

// OLD CODE - - - MAYBE LATER?
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
// // Id reference
// let dropdownMenu = document.getElementById("nav");
// let dropButton = document.getElementById("dropDownButton");

// // Drop menu when clicked
// dropButton.addEventListener("click", function (event) {
// 	event.stopPropagation();
// 	dropdownMenu.classList.toggle("hidden"); // Toggle hidden class on menu
// });
// // Close menu when user clicks outside of it
// window.addEventListener("click", function (event) {
// 	dropdownMenu.classList.add("hidden"); // Add hidden class to menu
// });
// //
//
//
//
//
// let getButton = document.getElementById("supplierGet");
// let getButtons = document.getElementById("get-all-suppliers");
// let getButtons2 = document.getElementById("get-supplier-count");
// let getButtons3 = document.getElementById("clear");

// getButton.addEventListener("click", function (event) {
// 	event.stopPropagation();
// 	getButtons.classList.toggle("hidden");
// 	getButtons2.classList.toggle("hidden");
// 	getButtons3.classList.toggle("hidden");
// });
//
//
//
//
//
// Table Page Selection
// Table Page Selection
