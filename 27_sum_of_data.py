data = '123456'

sum = 0
for digit in data:
    # print(digit)
    int_digit = int(digit)
    sum = sum + int_digit

print(f"The sum of the digits '{data}' is {sum}")
