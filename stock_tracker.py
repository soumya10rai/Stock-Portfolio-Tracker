# stock_tracker.py

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2000,
    "AMZN": 135,
    "NFLX": 400
}

stock_name = input("Enter the stock name (e.g., AAPL, TSLA): ").upper()
quantity = int(input("Enter the quantity you own: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_value = price * quantity
    print(f"\nTotal investment in {stock_name}: ₹{total_value}")

    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: ₹{total_value}\n")

    print("📄 Investment saved to portfolio.txt")

else:
    print("\nStock not found in the database.")
