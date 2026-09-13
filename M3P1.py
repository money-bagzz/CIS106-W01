print("Enter the stock ticker symbol:")
ticker_symbol = str(input())

print("Enter the number of shares:")
shares = int(input())

print("Enter the cost per share:")
cost_shares = float(input())

invested = shares * cost_shares
print("The amount of money invested is: $" + str(invested))