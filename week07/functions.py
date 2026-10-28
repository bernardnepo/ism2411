# Questions:
# 1) The first bug I understood was total = sale. The problem was that total
# was being replaced by each new sale instead of adding the sales together.
# Looking at the value of total during each loop helped me understand the bug.
# This showed me that tracing variable values is useful when debugging.

# 2) It takes two inputs: the original price and the
# customer's membership tier. It checks the tier and applies the correct
# discount. Gold receives 15% off, silver receives 10% off, bronze receives
# 5% off, and any other tier receives no discount. The function returns the
# discounted price.

# AI Disclosure:
# I used ChatGPT to help explain the errors in the debugging exercise and
# review how the functions and loops work. I used the explanations to better
# understand the code instead of only copying the answers.


# Exercise 1

def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


price = 200

print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")


# Exercise 3

discounted_price = apply_discount(200, "gold")
tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# Exercise 4

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5

sales = [120, 80, 250, 175, 90]

# Bug 1:
# The original code used total = sale, which replaced total each time.
# I changed it to += so each sale is added to the running total.
total = 0
for sale in sales:
    total += sale

print(f"Total: ${total}")


# Bug 2:
# The original for loop was missing a colon after "sales".
count = 0
for sale in sales:
    count += 1

print(f"Count: {count}")


# Bug 3:
# The original loop used <=, which eventually tried to access sales[5].
# Since the valid indexes are 0 through 4, I changed <= to <.
i = 0

while i < len(sales):
    print(sales[i])
    i += 1


# Exercise 6

x = 100   # global variable


def double_it():
    x = 999   # local variable
    return x * 2


print(x)
print(double_it())
print(x)

# Scope explanation:
# Scope means where a variable can be used.
# A variable created inside a function is local to that function.
# It does not change a variable with the same name outside the function.