import random

random_number = random.randint(1, 100)
print("You have 5 chance to guess the correct number\n")


chance = 5

for i in range(chance):

    guess = int(input("Enter your guess: \n"))
    chance = chance - 1

    if guess < random_number:
        print(f"Your guess is lesser than the random number.\033[91m\nYou have {chance} turns left\033[0m\n")
    elif guess > random_number:
        print(f"Your guess is greater than the random number.\033[91m\nYou have {chance} turns left\033[0m\n")
    else:
        print(f"Congratulations!!!!!! Your guess is correct\n")
        break

if chance == 0: 
        print(f"You used all of your chances. The correct random number is {random_number}")