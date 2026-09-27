print("Enter the number of books to order:")
books = int(input())
print("Enter the cost per book:")
cost = float(input())

order_total = books * cost
if(order_total > 50.00):
    shipping = 0.0
else:
    shipping = 25.0
    
print("Order Total:\n$" +
      str(order_total) + 
      "\nShipping fee:\n$" + 
      str(shipping))
