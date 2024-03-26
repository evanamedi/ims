let body = document.getElementById("main");

body.addEventListener("mousemove", function (event) {
	let x = event.clientX;
	let y = event.clientY;
	let blue = 140 + (y % 10);
	let green = 100 + (y % 40);
	let rgb = `rgb(0, ${green}, ${blue})`;
	body.style.background = `radial-gradient(circle 100px at ${x}px ${y}px, ${rgb}, black)`;
});
