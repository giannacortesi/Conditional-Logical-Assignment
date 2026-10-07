# Problem 1: Customer Discount Eligibility
# Concepts: nested if/elif/else, percentage, f-string formatting

purchase_amount = float(input("Purchase amount: "))
membership = input("Are you a member? (yes/no): ").strip().lower()

# Members get a discount at every purchase level; non-members only at $150+
if membership == "yes":
    if purchase_amount >= 100:
        discount_percent = 15
    else:
        discount_percent = 5
else:
    if purchse_amount >= 150:
        discount_percent = 10
    else:
        discount_percent = 0

# Final price = purchase minus the discount amount
final_price = purchase_amount * (1 - discount_percent / 100)

print(f"Discount applied: {discount_percent}%")
print(f"Final price: ${final_price:,.2f}")