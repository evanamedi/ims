const createObjectMapping = {
	suppliers: ["supplier_name", "supplier_address", "supplier_contact"],
	products: [
		"supplier_id",
		"product_name",
		"product_description",
		"product_price",
		"product_quantity",
	],
	customers: ["customer_name", "customer_contact", "customer_contact"],
	orders: [
		"order_product_id",
		"order_customer_id",
		"order_date",
		"order_quantity",
	],
	sales: [
		"sale_product_id",
		"sale_customer_id",
		"sale_date",
		"sale_quantity",
	],
};

const tableHeadersMapping = {
	suppliers: [
		"Supplier ID",
		"Supplier Name",
		"Supplier Address",
		"Supplier Contact",
	],
	products: [
		"Product ID",
		"Supplier ID",
		"Product Name",
		"Description",
		"Price",
		"Quantity",
	],
	customers: [
		"Customer ID",
		"Customer Name",
		"Customer Address",
		"Customer Contact",
	],
	orders: [
		"Order ID",
		"Product ID",
		"Customer ID",
		"Order Date",
		"Order Quantity",
	],
	sales: [
		"Sale ID",
		"Product ID",
		"Customer ID",
		"Sale Date",
		"Sale Quantity",
	],
};
