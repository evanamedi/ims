// Get the checkbox element
const toggleB = document.getElementById("toggleB");

// Get the image element
const imgElement = document.getElementById("logo");

// Set the initial state of the checkbox based on what's in localStorage
toggleB.checked = localStorage.getItem("darkMode") === "true";

// Apply the dark mode class and change the image source if needed
if (toggleB.checked) {
	document.documentElement.classList.add("dark");
	imgElement.src = "/static/imslogo-dark.png";
} else {
	document.documentElement.classList.remove("dark");
	imgElement.src = "/static/imslogo.png";
}

// Listen for changes on the checkbox
toggleB.addEventListener("change", function () {
	// If the checkbox is checked, enable dark mode and change the image source
	if (this.checked) {
		document.documentElement.classList.add("dark");
		imgElement.src = "/static/imslogo-dark.png";
		localStorage.setItem("darkMode", "true");
	}
	// Otherwise, disable dark mode and change the image source
	else {
		document.documentElement.classList.remove("dark");
		imgElement.src = "/static/imslogo.png";
		localStorage.setItem("darkMode", "false");
	}
});
