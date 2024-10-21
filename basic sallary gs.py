bs = float(input("Enter employee's basic salary: "))
da = (30 / 100) * bs
hra = (10 / 100) * bs
ta = (5 / 100) * bs
total = bs + da + hra + ta
print("Total salary of employee = ₹", total)

# Tax calculations
if total < 250000:
    print("Exempted from tax")
elif total <= 500000:
    tax_a = (total / 100) * 5
    print("Tax a = ₹", tax_a)
elif total <= 900000:
    tax_b = (total / 100) * 10
    print("Tax b = ₹", tax_b)
elif total <= 1200000:
    tax_c = (total / 100) * 15
    print("Tax c = ₹", tax_c)
elif total <= 1500000:
    tax_d = (total / 100) * 20
    print("Tax d = ₹", tax_d)
else:
    tax_e = (total / 100) * 30
    print("Tax e = ₹", tax_e)
