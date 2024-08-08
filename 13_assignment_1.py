#WAP to take user input email and validate whether it is correct email or not

user_imput_email = input("Enter email address: ")

if "@" in user_imput_email and ".com" in user_imput_email:
    print("Email is correct")
else:
    print("Email is incorrect")