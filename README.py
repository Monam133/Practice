import math

def calculate_triangle_area(a, b, c):
   
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


if a + b > c and a + c > b and b + c > a:
    area = calculate_triangle_area(a, b, c)
    print("The area of the triangle is:", area)
else:
    print("The sides do not form a valid triangle.")

