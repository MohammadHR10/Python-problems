# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}
programming = int(input("Enter the marks for programming: "))
marks.update({"input1":programming})
science = int(input("Enter the marks for science: "))
marks.update({"input2":science})
math = int(input("Enter the marks for math: "))
marks.update({"input3":math})

print(marks)


