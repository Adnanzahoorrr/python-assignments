angleone = float(input("Enter the first angle: "))
angletwo = float(input("Enter the second angle: "))
anglethree = float(input("Enter the third angle: "))

if angleone > 0 and angletwo > 0 and anglethree > 0:
    if angleone + angletwo + anglethree == 180:
        print("xyz is a triangle")
    else:
        print("xyz is not a triangle")
else:
    print("Angles must be positive")