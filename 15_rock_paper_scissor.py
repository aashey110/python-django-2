choice = ['rock', 'paper', 'scissor']

user1_choice = input("Enter the choice for user1: ")
user2_choice = input("Enter the choice for user2: ")

print(f"User1 choice = {user1_choice}")
print(f"User1 choice = {user2_choice}")

if user1_choice == user2_choice:
    print("The game tied")

elif (user1_choice == "rock" and user2_choice == "scissor") or (user1_choice == "scissor" and user2_choice == "paper") or (user1_choice == "paper" and user2_choice == "rock"):
    print("User1 wins")
else:
    print("User2 wins")