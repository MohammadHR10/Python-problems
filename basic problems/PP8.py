# Write a program to find the greatest of 3 numbers entered by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a >= b and a>=c):
    print("a is the largest number")
elif (b >= c):
    print("b is the largest number")
else:
    print("c is the largest number")