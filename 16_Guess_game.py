import random

random_number = random.randint(1, 100)
print("You have 5 chance to guess the correct number\n")


chance = 5

for i in range(chance):

    guess = int(input("Enter your guess: \n")) 
    if guess < random_number:
        print(f"Your guess is lesser than the random number. You have {chance - 1} turns left\n")
    elif guess > random_number:
        print(f"Your guess is greater than the random number. You have {chance - 1} turns left\n")
    else:
        print(f"Congratulations!!!!!! Your guess is correct\n")
        break
    if i == chance - 1:
        print(f"You used all of your chances. The correct random number is {random_number}")