"""
Stock Portfolio Simulator
Author: Your Name
Description:
    A simple stock portfolio simulator that:
    - Takes stock input from the user
    - Simulates current stock prices
    - Calculates profit/loss for each stock
    - Shows total portfolio performance
"""

import random


portfolio = [] 
n = int(input("How many stocks do you want to add? "))

for i in range(n):
    name = input(f"\nEnter stock name {i+1}: ")
    qty = int(input("Enter quantity: "))
    buy_price = float(input("Enter buy price per share: "))
    portfolio.append({"name": name, "quantity": qty, "buy_price": buy_price})


for stock in portfolio:
    stock["current_price"] = round(random.uniform(0.5, 1.5) * stock["buy_price"], 2)


for stock in portfolio:
    investment = stock["quantity"] * stock["buy_price"]
    current_value = stock["quantity"] * stock["current_price"]
    profit_loss = current_value - investment
    stock["pnl"] = round(profit_loss, 2)
    stock["pnl_percent"] = round((profit_loss / investment) * 100, 2)


total_investment = sum(s["quantity"] * s["buy_price"] for s in portfolio)
total_value = sum(s["quantity"] * s["current_price"] for s in portfolio)
total_pnl = total_value - total_investment

print("\n--- Portfolio Summary ---")
for stock in portfolio:
    print(
        f"{stock['name']} | Qty: {stock['quantity']} | Buy: {stock['buy_price']} "
        f"| Current: {stock['current_price']} | PnL: {stock['pnl']} ({stock['pnl_percent']}%)"
    )

print("\n--- Overall Performance ---")
print(f"Total Investment: {total_investment}")
print(f"Current Value: {total_value}")
print(f"Total Profit/Loss: {total_pnl}")
