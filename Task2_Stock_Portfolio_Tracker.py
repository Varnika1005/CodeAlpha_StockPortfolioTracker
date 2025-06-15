# Stock Portfolio Tracker

# Hardcoded stock prices
import os

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 320,
    "META": 1000,
    "NVDA": 2300,
    "AMZN": 1400
}

# Dictionary to store user's stocks and quantities
portfolio = {}

print("\n=== Stock Portfolio Tracker ===")
print("Enter your stocks and quantities. Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT, META, NVDA, AMZN): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    quantity_input = input(f"Enter quantity for {stock}: ")
    if not quantity_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    quantity = int(quantity_input)
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock in portfolio:
    quantity = portfolio[stock]
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock} - {quantity} shares @ ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional Save to a file option
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == 'yes':
    filename = "portfolio_report.txt"
    file = open(filename, "w")
    file.write("Stock Portfolio Report\n")
    for stock in portfolio:
        quantity = portfolio[stock]
        price = stock_prices[stock]
        value = price * quantity
        file.write(f"{stock} - {quantity} shares @ ${price} = ${value}\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")
    file.close()
    print(f"Report saved to {filename}")
    # Open's the file automatically
    os.system(f"open {filename}")
