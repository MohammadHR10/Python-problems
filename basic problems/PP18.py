# Search for a number x in this tuple using loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#n = int(input("Enter the number you want to search: "))
x = 9
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found", nums[i])
    i += 1