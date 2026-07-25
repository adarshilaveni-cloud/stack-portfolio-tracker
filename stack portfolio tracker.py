# Stock Portfolio Tracker

# Dictionary of stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2800,
    "HDFC": 1700,
    "WIPRO": 450,
    "ICICI": 950,
    "SBI": 850
}

portfolio = {}
total_value = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

n = int(input("Enter the number of stocks you own: "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available in price list.")

print("\n")
print("=" * 40)
print("YOUR PORTFOLIO")
print("=" * 40)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(f"{stock}")
    print(f"Price    : ₹{price}")
    print(f"Quantity : {quantity}")
    print(f"Value    : ₹{value}")
    print("-" * 40)

print(f"Total Portfolio Value = ₹{total_value}")
print("=" * 40)

choice = input("\nDo you want to save the report? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(f"{stock}\n")
            file.write(f"Price : ₹{price}\n")
            file.write(f"Quantity : {quantity}\n")
            file.write(f"Value : ₹{value}\n")
            file.write("-" * 40 + "\n")

        file.write(f"\nTotal Portfolio Value = ₹{total_value}")

    print("Report saved successfully as portfolio_report.txt")

print("\nThank you for using Stock Portfolio Tracker!")