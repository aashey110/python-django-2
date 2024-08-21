i = 1
check_time = int(input("Enter the number of times you want to check the temperature: "))
while i <= check_time:
    temp = int(input("Enter the temperature: "))
    i = i + 1
    if temp > 30:
        print("Turn your AC on")
        break