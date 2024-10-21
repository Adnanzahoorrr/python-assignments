import math

def quad(a, b, c):
    r1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/2 * a
    r2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c))/2 * a
    return [r1, r2]
print("For a quadratic equation, ax^2 + bx + c: \n")
x = int(input("Enter the first constant, a: "))
y = int(input("Enter the second constant, b: "))
z = int(input("Enter the third constant, c: "))
if(math.pow(y, 2) - 4 * x * z) < 0:
    print("The quadratic equation does not have real roots.")
else:
    print("The roots for the given equation are: ", quad(x, y, z))