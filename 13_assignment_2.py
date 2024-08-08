#WAP to take user input mark percentage and find their division

percentage = int(input("Enter your percentage: "))

if percentage > 100:
    print("Invalid percentage! Percentage should be between 0 to 100")

elif percentage >= 90:
    print("You've scored distinction")

elif percentage < 90 and percentage >= 80:
    print("First division")

elif percentage < 80 and percentage >= 60:
    print("Second division")

elif percentage < 60 and percentage >= 40:
    print("Third division")

else:
    print("You've failed")
    