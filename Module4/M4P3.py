print("Enter the total for your meal:")
total = float(input())
# I used a for-loop here for convenience.
for discount in [15, 18, 20]:
    tip_amt = total * (discount * 0.01)
    total_tip = total + tip_amt
    
    print("With a " + str(discount) + "% Tip:\n")
    print("Total:\t" + str(total))
    print("Tip:\t" + str(tip_amt))
    print("Total with Tip:\t" + str(tip_amt) + "\n")