# Search for a number x in this tuple using loop:

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

index = 0
for numbers in num:
    #if (numbers == num[6]):
    if (numbers == x):
        print("Found at index", index)
        break
    index += 1
    #print(numbers)
