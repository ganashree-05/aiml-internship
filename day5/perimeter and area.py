from measurements import Measurements

length = int(input("Enter length: "))
width = int(input("Enter width: "))

obj = Measurements()

print("The area is:", obj.area(length, width))
print("The perimeter is:", obj.perimeter(length, width))