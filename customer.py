# ISM2411 - Lab 11
# Name: Bernard N.Bezerra

# REFLECTION 1)
# In real work, I would use .get() when information might be missing,
# such as a customer's email or phone number, because it prevents errors.
# I would use bracket notation when a field is required, such as a
# customer ID, because missing required information should raise an error.

# REFLECTION 2)
# Exercise 8 reminds me of Excel PivotTables, where we group data
# by categories and calculate totals, such as sales by region.
# Python can be more useful for large datasets because it allows us
# to automate the process and repeat the analysis with new data.


# EXERCISE 1 

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print("EXERCISE 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2 

print("\nEXERCISE 2")

customer["phone"] = "813-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 

print("\nEXERCISE 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), iterating over a dictionary returns only its keys.
for key in customer:
    print(key)


# EXERCISE 5 

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

original_price = 200
final_price = original_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6 

print("\nEXERCISE 6")

customers = [
    customer,
    {
        "name": "Bob",
        "tier": "silver",
        "ytd_spend": 500
    },
    {
        "name": "Charlie",
        "tier": "bronze",
        "ytd_spend": 200
    }
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name} | Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 

print("\nEXERCISE 7")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# EXERCISE 8

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
