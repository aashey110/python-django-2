# # # # # user_input = int(input("Enter a number:"))
# # # # # if user_input%2 == 0:
# # # # #     print("it is even")
# # # # # else:
# # # # #     print("odd")

# # # #find highest digit
# # # # input_string = "0124392566"

# # # # highest_digit = 0

# # # # for digit in input_string:
# # # #     if int(digit) > highest_digit:
# # # #         highest_digit = int(digit)
        
# # # # print(f"The highest digit in {input_string} is {highest_digit}")

# # # # lowest_digit = 99
# # # # for digit in input_string:
# # # #     if int(digit) < lowest_digit:
# # # #         lowest_digit = int(digit)

# # # # print(f"The highest digit in {input_string} is {lowest_digit}")

# # # #count word
# # # word = input("Enter a sentence: ")
# # # word = word.split()
# # # print(f"The number of words in the sentence is {len(word)}")

# # input_iteger = int(input("Enter an integer:"))
# # str_input_integer = str(input_iteger)
# # sum = 0
# # for i in str_input_integer:
# #     sum = sum + int(i)

# # print(sum)

# #reverse a string
# input_string = "Python"
# print(input_string[::-1])

input_string = input("Enter a word: ")
reverse_string = input_string[::-1]
if input_string == reverse_string:
    print("it is palindrome word")
else:
    print("it is not palindrome word")
