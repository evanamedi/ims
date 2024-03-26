function appendData(row, product) {
	var order = [
		"id",
		"supplier_id",
		"product_name",
		"product_description",
		"product_price",
		"product_quantity",
	];
	order.forEach(function (key) {
		row.append("<td>" + product[key] + "</td>");
	});
}

function sendRequest(url, type, data) {
	$.ajax({
		url: url,
		type: type,
		contentType: "application/json",
		data: JSON.stringify(data),
		success: function (response) {
			var products = response.data;
			var table = $("<table class='table'>");
			table.append(
				"<tr><th>ID</th><th>Supplier ID</th><th>Product</th><th>Description</th><th>Price</th><th>Quantity</th></tr>"
			);
			products.forEach(function (product) {
				var row = $("<tr>");
				appendData(row, product);
				table.append(row);
			});
			$("#result").html(table);
		},
		error: function (response) {
			$("#result").html(JSON.stringify(response));
		},
	});
}

$("#delete-form").submit(function (event) {
	event.preventDefault();

	var id = $("#delete-id").val();

	sendRequest(`http://localhost:5000/v1/product/delete/${id}`, "DELETE", {});
});

$("#add-form").submit(function (event) {
	event.preventDefault();

	var supplier = $("#supplier_id").val();
	var name = $("#name").val();
	var description = $("#description").val();
	var price = $("#price").val();
	var quantity = $("#quantity").val();

	sendRequest(`http://localhost:5000/v1/product`, "POST", {
		supplier_id: supplier,
		product_name: name,
		product_description: description,
		product_price: price,
		product_quantity: quantity,
	});
});

$("#get-form").submit(function (event) {
	event.preventDefault();

	var id = $("#get-id").val();

	sendRequest(`http://localhost:5000/v1/product/${id}`, "GET", {});
});

$("#update-form").submit(function (event) {
	event.preventDefault();

	var id = $("#update-id").val();
	var field = $("#field").val();
	var newValue = $("#new-value").val();

	sendRequest(`http://localhost:5000/v1/product/${id}/${field}`, "PUT", {
		new_value: newValue,
	});
});

$("#get-all").click(function () {
	sendRequest(`http://localhost:5000/v1/product/all`, "GET", {});
});

$("#get-name-form").submit(function (event) {
	event.preventDefault();

	var name = $("#search-name").val();
	sendRequest(`http://localhost:5000/v1/product/name/${name}`);
});
