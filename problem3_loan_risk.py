# Problem 3: Loan Risk Classification
# Concepts: if/elif/else with the logical operator "and"

credit_score = int(input("Credit score: "))
annual_income = float(input("Annual income: "))

# Check the strictest category first; "and" requires BOTH conditions to be true
if credit_score >= 720 and annual_income >= 60000:
    risk_category = "Low Risk"
elif credit_score >= 650 and annual_income >= 40000:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

print(f"Loan Risk Category: {risk_category}")