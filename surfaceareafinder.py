import math

radius = int(input("Enter radius of the sphere\n"))
surfaceArea = (4 * math.pi * math.pow(radius, 2))
volume = ((4 / 3) * math.pi * math.pow(radius, 3))

print("The volume of a sphere with a radius of ", radius, "is = ", volume)
print("The Surface Area of a sphere with a radius of ", radius, "is = ", surfaceArea)
