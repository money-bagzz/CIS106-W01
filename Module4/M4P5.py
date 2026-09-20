print("Enter the fixed cost:")
fixed_cost = float(input())

print("Enter the price per unit:")
price_per_unit = float(input())

print("Enter the cost per unit:")
cost_per_unit = float(input())

break_even = fixed_cost / (price_per_unit - cost_per_unit)
print("The break even point is: $" + str(break_even))