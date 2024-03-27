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

//
//
//

// Buttons for fields (create, update, delete, etc...)
