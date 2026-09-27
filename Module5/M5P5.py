print("Enter your last name:")
last_name = str(input())

print("\nEnter number of dependents:")
dependents = int(input())

print("\nEnter your gross income:")
gross_income = float(input())

adjust_gross_income = gross_income - (dependents * 12000)
if(adjust_gross_income > 50000):
    tax_rate = 0.2
else:
    tax_rate = 0.1
    
income_tax = adjust_gross_income * tax_rate
if(income_tax < 0):
    income_tax = 100.0

print("\nLast name:\n" +
      str(last_name) + 
      "\nGross income:\n" +
      str(gross_income) + 
      "\n# of dependents:\n" +
      str(dependents) +
      "\nAdjusted gross income:\n" +
      str(adjust_gross_income) + 
      "\nIncome tax:\n" +
      str(income_tax))