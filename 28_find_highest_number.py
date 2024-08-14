data = "872027513"

highest_digit = 0

for digit in data:
    if int(digit) > highest_digit:
        highest_digit = int(digit)
        
print(f"The highest digit in {data} is {highest_digit}")