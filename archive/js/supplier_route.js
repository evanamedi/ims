function appendData(row, supplier) {
	var order = ["id", "supplier_name", "supplier_address", "supplier_contact"];
	order.forEach(function (key) {
		row.append("<td>" + supplier[key] + "</td>");
	});
}

function sendRequest(url, type, data) {
	$.ajax({
		url: url,
		type: type,
		contentType: "application/json",
		data: JSON.stringify(data),
		success: function (response) {
			if (type == "DELETE") {
				$("#result").html(response.message);
			} else {
				var suppliers = response.data;
				var table = $("<table class='table'>");
				table.append(
					"<tr><th>ID</th><th>Name</th><th>Address</th><th>Contact</th></tr>"
				);
				suppliers.forEach(function (supplier) {
					var row = $("<tr>");
					appendData(row, supplier);
					table.append(row);
				});
				$("#result").html(table);
			}
		},
		error: function (response) {
			$("#result").html(JSON.stringify(response));
		},
	});
}

$("#delete-form").submit(function (event) {
	event.preventDefault();

	var id = $("#delete-id").val();

	sendRequest(`http://localhost:5000/v1/supplier/delete/${id}`, "DELETE", {});
});

$("#add-form").submit(function (event) {
	event.preventDefault();

	var name = $("#name").val();
	var address = $("#address").val();
	var contact = $("#contact").val();

	sendRequest(`http://localhost:5000/v1/supplier`, "POST", {
		supplier_name: name,
		supplier_address: address,
		supplier_contact: contact,
	});
});

$("#get-form").submit(function (event) {
	event.preventDefault();

	var id = $("#get-id").val();

	sendRequest(`http://localhost:5000/v1/supplier/${id}`, "GET", {});
});

$("#update-form").submit(function (event) {
	event.preventDefault();

	var id = $("#update-id").val();
	var field = $("#field").val();
	var newValue = $("#new-value").val();

	sendRequest(`http://localhost:5000/v1/supplier/${id}/${field}`, "PUT", {
		new_value: newValue,
	});
});

$("#get-all").click(function () {
	sendRequest(`http://localhost:5000/v1/supplier/all`, "GET", {});
});

$("#get-name-form").submit(function (event) {
	event.preventDefault();
	var name = $("#search-name").val();
	sendRequest(`http://localhost:5000/v1/supplier/name/${name}`, "GET");
});
