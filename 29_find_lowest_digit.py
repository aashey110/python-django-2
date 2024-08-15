data = "87221755756547"

lowest_digit = 9

for digit in data:
    if int(digit) < lowest_digit:
        lowest_digit = int(digit)
        
print(f"The lowest digit in {data} is {lowest_digit}")