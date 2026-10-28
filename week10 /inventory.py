# ISM2411 - Python for Business
# Module 10 - Inventory List Manager
# Bernard Nepomuceno Bezerra

# REFLECTION

# 1) What surprised me most about Python lists is how easy it is to
# organize and modify multiple items using just one variable.
# I also found it interesting that I can use indexing and slicing
# to access specific items without having to go through the entire list.

# 2) During my summer resale business project, I bought and sold PS5 consoles.
# Python lists could have helped me organize product prices,
# calculate average selling prices, and identify my most profitable
# sales instead of manually tracking everything in Excel.


# Exercise 1 

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1:")
print(inventory)
print(len(inventory))


# Exercise 2 

print("\nExercise 2:")

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3 

print("\nExercise 3:")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4 

print("\nExercise 4:")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5 

print("\nExercise 5:")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for coordinates because it prevents accidental changes.")

print(coords)


# Exercise 6 

print("\nExercise 6:")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7 

print("\nExercise 7:")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)


# Exercise 8 

print("\nExercise 8:")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))
