
  # Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

portfolio = {}

def show_menu():
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Calculate Total Investment")
    print("4. Save Portfolio to File")
    print("5. Exit")
    print("=" * 35)

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # 1. Add Stock
    if choice == "1":
        stock = input("Enter stock symbol: ").upper()

        if stock not in stock_prices:
            print("Stock not available!")
            continue

        quantity = int(input("Enter quantity: "))

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"{stock} added successfully!")

    # 2. View Portfolio
    elif choice == "2":
        if not portfolio:
            print("Portfolio is empty.")
        else:
            print("\nYour Portfolio:")
            for stock, qty in portfolio.items():
                print(f"{stock}: {qty} shares")

    # 3. Calculate Total Investment
    elif choice == "3":
        total = 0
        for stock, qty in portfolio.items():
            total += stock_prices[stock] * qty

        print(f"\nTotal Investment Value: ${total}")

    # 4. Save Portfolio to File
    elif choice == "4":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares = ${value}\n")

        print("Portfolio saved successfully!")

    # 5. Exit
    elif choice == "5":
        print("Exiting Stock Portfolio Tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1 and 5.")
