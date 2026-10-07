# Problem 2: Emoloyee Performance Bonus
# Concepts: if/elif/else chain, percentages, f-string formatting

annual_salary = float(input("Annual salary: "))
performance_score = float(input("Performance score (0-100): "))

# Check from highest score down; the first true condition wins
if performance_score >= 90:
    bonus_percent = 20
elif performance_score >= 80:
    bonus_percent = 10
elif performance_score >= 70:
    bonus_percent = 5
else:
    bonus_percent = 0

# Bonus is a percentage of salary
bonus_amount = annual_salary * bonus_percent / 100

print(f"Performance Bonus: {bonus_percent}%")
print(f"Bonus Amount: ${bonus_amount:,.2f}")