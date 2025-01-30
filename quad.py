#this program tells you how many real solutions exist for your quadratic formula and what they are if the solutions exist 

import math
print("Given a quadratic equation of the form a * x^2 + b * x + c")

#get inputs a, b, and c from 
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

#create function to calculate determinant
def disc():
    d = b * b - 4 * a * c
    return d

d = disc()

#create function for calculating x values
def calc():
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2

#there are no solutions when the determinant is less than 0
if d < 0:
    print("There are no real solutions")

#there is 1 solution when the determinant is 0
elif d == 0:
    x1, x2 = calc()
    print(f"There is one real solution: {x1:.2f}")

#there are no 2 when the determinant is greater than 0
else:
    x1, x2 = calc()
    print(f"There are 2 real solutions\nSolution 1: {x1:.2f}\nSolution 2: {x2:.2f}")
