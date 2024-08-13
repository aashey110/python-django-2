number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number != 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10

if original_number == reversed_number:
        print(original_number,"is a palindrome number")
else:
        print(original_number,"is not a palindrome number")
