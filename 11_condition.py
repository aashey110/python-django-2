'''make a program which take  input as age and print they
 adult or not'''

age = int(input("Enter your age:"))
if age > 18:
    print("You are adult because", age , "is greater than 18")
else:
    print("You are not adult because", age , "is less than 18")