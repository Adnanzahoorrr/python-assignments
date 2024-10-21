sidea= float(input("Enter the length of side a: "))
sideb= float(input("Enter the length of side b: "))
sidec = float(input("Enter the length of side c: "))
if sidea == sideb == sidec:
    print("The triangle is equilateral.")
elif sidea == sideb or sideb == sidec or sidea ==sidec:
    print ("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

