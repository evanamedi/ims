// ---------- SELECT TABLE MENU ----------
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

let testButton = document.getElementById("testButton");
let testMenu = document.getElementById("testMenu");

testButton.addEventListener("click", function (event) {
	event.stopPropagation();
	testMenu.classList.toggle("hidden");
});

window.addEventListener("click", function (event) {
	testMenu.classList.add("hidden");
});
