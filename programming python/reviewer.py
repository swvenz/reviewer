# Triangle Identifier Program

# Input three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if it forms a triangle first (Triangle Inequality)
if a + b > c and a + c > b and b + c > a:
    # Check for Equilateral
    if a == b and b == c:
        print("Equilateral Triangle")
    # Check for Isosceles
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    # Check for Scalene (each side differs by 1)
    elif (a == b + 1 and b == c + 1) or (b == a + 1 and a == c + 1) or (c == a + 1 and a == b + 1) or \
         (a == c + 1 and c == b + 1) or (b == c + 1 and c == a + 1) or (c == b + 1 and b == a + 1):
        print("Scalene Triangle (each side differs by 1)")
    else:
        print("Triangle but not matching given conditions")
else:
    print("Not a Triangle")
