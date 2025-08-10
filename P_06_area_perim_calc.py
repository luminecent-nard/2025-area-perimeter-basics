#ask user for width and height
#assume they are correct
width = int(input("width: "))
height = int(input("height: "))
#calculate area and perimeter
area = height * width
perimeter = 2 * (height + width)
#output area and perimeter
print(f"area = {area}")
print(f"perimeter = {perimeter}")