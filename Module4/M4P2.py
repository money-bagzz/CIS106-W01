print("Input the price per share:")
price_per_share = float(input())

print("Input the current stock price:")
stock_price = float(input())

print("Input the quantity of stock:")
quantity = int(input())

stock_value = (stock_price - price_per_share) * quantity
if(stock_value > 0):
    print("The increase in value of the stock entered is: $" 
          + str(stock_value))
elif(stock_value == 0):
    print("The value of the stock entered did not change.")
else:
    # I used abs() here so I could put the negative sign behind the $ symbol
    print("The decrease in value of the stock entered is: -$" 
          + str(abs(stock_value)))