import math

print("**************************************")
print("Select 1 for calculation triangle area")
print("Select 2 for calculation square area")
print("Select 3 for calculation circle area")
print("**************************************")
print("\n")

# function

def triangle(base, high):
  return 1/2 * base * high

def square(width, length):
  return width * length

def circle(radius):
  return math.pi * math.pow(radius, 2)

check_correct_function = False
while not check_correct_function:
  select_function = input("Enter your function: ")
  if select_function == '1':
    print("You select calculation triangle area\n")
    base = input("Enter your base: ")
    high = input("Enter your hight: ")
    area = triangle(float(base), float(high))
    print("Area is {:.2f}".format(area))
    check_correct_function = True
  elif select_function == '2':
    print("You select calculation square area\n")
    width = input("Enter your width: ")
    lenght = input("Enter your lenght: ")
    area = square(float(width), float(lenght))
    print("Area is {:.2f}".format(area))
    check_correct_function = True
  elif select_function == '3':
    print("You select calculation circle area\n")
    radius = input("Enter your radius: ")
    area = circle(float(radius))
    print("Area is {:.2f}".format(area))
    check_correct_function = True
  else:
    print("Please select 1, 2 or 3\n")