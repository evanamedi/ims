// ---------- INITIALIZE BUTTONS ----------
let createButton = document.getElementById("createButtonID");
let updateButton = document.getElementById("updateButtonID");
let getByIdButton = document.getElementById("getByIdButtonID");
let deleteButton = document.getElementById("deleteButtonID");

// ---------- INITIALIZE FORMS ----------
let createForm = document.getElementById("createFormID");
let updateForm = document.getElementById("updateFormID");
let getForm = document.getElementById("getFormID");
let deleteForm = document.getElementById("deleteFormID");

// ---------- TOGGLE CREATE FROM ----------
createButton.addEventListener("click", function (event) {
	event.stopPropagation();
	createFormFunction(true);
	deleteFormFunction(false);
	getFormFunction(false);
	updateFormFunction(false);
	testMenu.classList.toggle("hidden");
});
// toggle off
window.addEventListener("click", function (event) {
	if (!createForm.contains(event.target)) createFormFunction(false);
});

// ---------- TOGGLE UPDATE FROM ----------
updateButton.addEventListener("click", function (event) {
	event.stopPropagation();
	updateFormFunction(true);
	createFormFunction(false);
	getFormFunction(false);
	deleteFormFunction(false);
	testMenu.classList.toggle("hidden");
});
// toggle off
window.addEventListener("click", function (event) {
	if (!updateForm.contains(event.target)) updateFormFunction(false);
});

// ---------- TOGGLE GET FROM ----------
getByIdButton.addEventListener("click", function (event) {
	event.stopPropagation();
	getFormFunction(true);
	createFormFunction(false);
	updateFormFunction(false);
	deleteFormFunction(false);
	testMenu.classList.toggle("hidden");
});
// toggle off
window.addEventListener("click", function (event) {
	if (!getForm.contains(event.target)) getFormFunction(false);
});

// ---------- TOGGLE DELETE FROM ----------
deleteButton.addEventListener("click", function (event) {
	event.stopPropagation();
	deleteFormFunction(true);
	createFormFunction(false);
	updateFormFunction(false);
	getFormFunction(false);
	testMenu.classList.toggle("hidden");
});
// toggle off
window.addEventListener("click", function (event) {
	if (!deleteForm.contains(event.target)) deleteFormFunction(false);
});

// ---------- FUNCTIONS ----------

// CREATE BUTTON FUNCTION
function createFormFunction(bool) {
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

// UPDATE BUTTON FUNCTION
function updateFormFunction(bool) {
	if (bool) {
		return (
			updateForm.classList.toggle("hidden"),
			updateButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			updateForm.classList.add("hidden"),
			updateButton.classList.remove("toggleButton")
		);
	}
}

// GET BUTTON FUNCTION
function getFormFunction(bool) {
	if (bool) {
		return (
			getForm.classList.toggle("hidden"),
			getByIdButton.classList.toggle("toggleButton")
		);
	} else {
		return (
			getForm.classList.add("hidden"),
			getByIdButton.classList.remove("toggleButton")
		);
	}
}

// DELETE BUTTON FUNCTION
function deleteFormFunction(bool) {
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
