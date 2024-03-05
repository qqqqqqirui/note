import math
def calculate_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return root,
    else:
        return None
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

roots = calculate_roots(a, b, c)
if roots:
    if len(roots) == 2:
        print("The equation has two real roots:", roots)
    else:
        print("The equation has one real root:", roots[0])
else:
    print("The equation has no real roots.")
