import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Its a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You Win"
    else:
        return "Computer wins!"
    
def play_game():
    while True:
        user_choice = input("Enter Your Choice (rock, paper, scissors, or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("User quit")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid Choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(winner(user_choice, computer_choice))
        print()

play_game()

 

