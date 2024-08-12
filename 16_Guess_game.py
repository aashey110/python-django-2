import random

random_number = random.randint(1, 100)
guess = int(input("Enter your guess: "))


while guess != random_number:
    print(f"Your guess is incorrect because the correct number is {random_number}")
    break
else:
    print("Your guess is correct")