units = float(input("Enter the electricity units consumed: "))
if units <= 50:
    bill = units * 0.50
elif units <= 100:
    bill = units * 0.75
elif units <= 200:
    bill = units * 1.20
else:
    bill = units * 1.50

print(f"The total electricity bill is: Rs {bill:.2f}")
