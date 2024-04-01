# Write a program to check if a number entered by the user is odd or even

num = int(input("Enter an int: "))
if (num%2 == 0):
    print("The number is even")
elif (num%2 != 0):
    print("The number is odd")
else:
    print("Enter the number again")