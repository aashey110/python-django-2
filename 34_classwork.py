
while True:
    num1 = int(input("Enter first operand: "))
    num2 = int(input("Enter second operand: "))

    print("Select one of the following operation to be /performed:\n + (addition)\n-(substraction)\n* (multiplication)\n/ (division)")

    operator = input("Enter the operator: ")



    if operator == "+":
        sum = num1 + num2
        print(num1," + ", num2 , " = ", sum)

    elif operator == "-":
        difference = num1 - num2
        print(num1," - ", num2 , " = ", difference)

    elif operator == "*":
        product = num1 * num2
        print(num1," * ", num2 , " = ", product)

    elif operator == "/":
        quotient = num1 / num2
        print(num1," / ", num2 , " = ", quotient)

    else:
        print("Invalid operator, Please enter valid operator")


    choice = input("Do you want to calculate again? (y/n): " )
    if choice == 'n':
        break
