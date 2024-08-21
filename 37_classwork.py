num_list = [1,5,9,6,89,1203,4,23]

highest_digit = 0
for numbers in num_list:
    if numbers > highest_digit:
        highest_digit = numbers

print(f"Highest number = {highest_digit}")