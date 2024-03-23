// Id reference
let dropdownMenu = document.getElementById("nav");
let dropButton = document.getElementById("dropDownButton");

// Drop menu when clicked
dropButton.addEventListener("click", function (event) {
	event.stopPropagation();
	dropdownMenu.classList.toggle("hidden"); // Toggle hidden class on menu
});
// Close menu when user clicks outside of it
window.addEventListener("click", function (event) {
	dropdownMenu.classList.add("hidden"); // Add hidden class to menu
});
//
//
//
//
//
// CREATE SUPPLIER BUTTON
let createButton = document.getElementById("createID");
let createForm = document.getElementById("add-supplier");

createButton.addEventListener("click", function (event) {
	event.stopPropagation();
	createForm.classList.toggle("hidden");
	createButton.classList.toggle("toggleButton");
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	createForm.classList.add("hidden");
	createButton.classList.remove("toggleButton");
});
//
//
//
//
//
// UPDATE SUPPLIER BUTTON
let updateButton = document.getElementById("updateForm");
let updateField = document.getElementById("update-supplier-field");

updateButton.addEventListener("click", function (event) {
	event.stopPropagation();
	updateField.classList.toggle("hidden");
	updateButton.classList.toggle("toggleButton");
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	updateField.classList.add("hidden");
	updateButton.classList.remove("toggleButton");
});
//
//
//
//
//
// GET SUPPLIER BUTTON
let getSupplier = document.getElementById("getSupplierID");
let getFormID = document.getElementById("get-supplier-by-id");

getSupplier.addEventListener("click", function (event) {
	event.stopPropagation();
	getFormID.classList.toggle("hidden");
	getSupplier.classList.toggle("toggleButton");
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	getFormID.classList.add("hidden");
	getSupplier.classList.remove("toggleButton");
});
//
//
//
//
//
// DELETE SUPPLIER BUTTON
let deleteSupplierButton = document.getElementById("deleteSupplier");
let deleteForm = document.getElementById("delete-supplier");

deleteSupplierButton.addEventListener("click", function (event) {
	event.stopPropagation();
	deleteForm.classList.toggle("hidden");
	deleteSupplierButton.classList.toggle("toggleButton");
});
// TOGGLE OFF
window.addEventListener("click", function (event) {
	deleteForm.classList.add("hidden");
	deleteSupplierButton.classList.remove("toggleButton");
});

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
