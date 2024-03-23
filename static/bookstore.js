class Shop {
	constructor(initialBooks) {
		this.books = initialBooks;
		this.price = 10;
		this.sales = 0;
	}

	adjustPrice() {
		if (this.books < 20) {
			this.price += 2;
		} else if (this.books < 50) {
			this.price += 1;
		} else {
			this.price = Math.max(10, this.price - 1);
		}
	}

	restockBooks() {
		if (this.books < 20) {
			this.books += 50;
		}
	}

	update() {
		this.restockBooks();
		this.adjustPrice();
	}

	sellBook(weather) {
		if (this.books > 0 && (weather !== "rainy" || Math.random() < 0.5)) {
			this.books -= 1;
			this.sales += this.price;
			return this.price;
		} else {
			return 0;
		}
	}
}

class Customer {
	constructor() {
		this.money = 100;
		this.workDays = 0;
		this.attemptsToBuyWhileBroke = 0;
	}

	buyBook(shop, weather) {
		const price = shop.sellBook(weather);
		if (this.money >= price) {
			this.money -= price;
			return true;
		} else {
			this.attemptsToBuyWhileBroke += 1;
			return false;
		}
	}

	isBroke() {
		return this.money <= 0;
	}

	decideAction(shop, weather) {
		if (this.isBroke()) {
			if (this.attemptsToBuyWhileBroke > 3) {
				if (
					window.confirm(
						"This customer has tried to buy a book while broke more than 3 times. Send them to prison?"
					)
				)
					return "Prison";
			}
			if (Math.random() < 0.1) {
				if (
					window.confirm(
						"This customer is broke. Send them to work camp?"
					)
				) {
					this.work(shop);
				}
			}
		} else if (Math.random() < 0.4) {
			this.buyBook(shop, weather);
		}
	}

	work(shop) {
		if (this.workDays < 7) {
			shop.books += 10;
			shop.sales += 20;
			this.workDays += 1;
			this.money += 20;
		}
	}
}

function simulate() {
	const shop = new Shop(1000);
	let customers = [
		new Customer(),
		new Customer(),
		new Customer(),
		new Customer(),
		new Customer(),
	];
	let week = 0;
	let day = 0;

	const outputDiv = document.createElement("div");
	const containerDiv = document.getElementById("output");
	containerDiv.appendChild(outputDiv);

	function simulateDay() {
		const weather = determineWeather();
		processCustomerActions(customers, shop, weather);
		shop.update();
		updateOutput(outputDiv, shop, customers, week, weather);
		updateDayAndWeek();
		checkEndOfSimulation();

		function determineWeather() {
			return Math.random() < 0.5 ? "sunny" : "rain";
		}

		function processCustomerActions(customers, shop, weather) {
			customers.forEach((customer) => {
				const action = customer.decideAction(shop, weather);
				if (action === "Prison") {
					const index = customers.indexOf(customer);
					if (index > -1) {
						customers.splice(index, 1);
					}
				}
			});
		}

		function updateOutput(outputDiv, shop, customers, week, weather) {
			outputDiv.innerHTML += `Week ${week + 1}, ${
				weather.charAt(0).toUpperCase() + weather.slice(1)
			}: Sales = ${shop.sales}, Books left = ${shop.books}, Customers = ${
				customers.length
			}<br>`;
		}

		function updateDayAndWeek() {
			day += 1;
			if (day % 7 === 0) {
				week += 1;
			}
		}

		function checkEndOfSimulation() {
			if (day < 90) {
				setTimeout(simulateDay, 100);
			} else {
				outputDiv.innerHTML += `<br><strong>Simulation ended.</strong><br>Total Sales = ${shop.sales}, Remaining Books = ${shop.books}, Total Customers = ${customers.length}<br>`;
			}
		}
	}
	simulateDay();
}

document.getElementById("startButton").addEventListener("click", simulate);
