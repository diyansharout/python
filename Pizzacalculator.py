# Ask the person how many pizza slices they want #eval = evaluated (solve)
number_of_pizzas = eval(input("How many pizzas do you want?"))
# Ask for the menu cost of each pizza.
cost_per_pizza = eval(input("How much does each pizza cost?"))
# Calculate the total cost of the pizzas as por subtotal
subtotal = number_of_pizzas * cost_per_pizza
# Calculate the sales tax owned, at 8 percent of out subtotal
tax_rate = 0.08  # Store 8% of the subtotal
sales_tax = subtotal * tax_rate
# Add the sales tax to the subtotal for the final total
total = subtotal + sales_tax
# Show to user the total amount due, including the tax
print("The total cost of the pizza is $", total)
print("This includes the subtotal $", subtotal)
print(" And $", sales_tax, "in the sales tax")

