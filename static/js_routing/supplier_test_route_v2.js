// HTML FORM
//
// <form id="create-supplier">
//     <input type="text" name="supplier_name" required>
//     <input type="text" name="supplier_address" required>
//     <input type="text" name="supplier_contact" required>
//     <input type="submit" value="Submit">
// </form>
//

const form = document.getElementById("create-supplier");

form.addEventListener("submit", function (event) {
	event.preventDefault();

	const formData = new FormData(form);
	const data = Object.fromEntries(formData);

	fetch(`http://localhost:5000/v2/supplier`, {
		method: "POST",
		headers: {
			"Content-type": "application/json",
		},
		body: JSON.stringify(data),
	})
		.then((response) => response.json())
		.then((data) => console.log(data))
		.catch((error) => {
			console.error("Error", error);
		});
});

//
// If form input is like so in their respective order:
// IMC Inc
// 123 Main St
// 0123456789
//
// JSON Object sent to API in this instance
//
// {
//     "supplier_name": "IMC Inc",
//     "supplier_address": "123 Main St",
//     "supplier_contact": "0123456789"
// }
//
