def calculate_bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        return 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6

units = float(input("Enter units consumed: "))
bill = calculate_bill(units)

if bill > 1000:
    discount = bill * 0.10
    bill -= discount
    print(f"Applied 10% discount: ₹{discount:.2f}")

print(f"Total electricity bill: ₹{bill:.2f}")
