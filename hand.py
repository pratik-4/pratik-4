import random

options = [
    "stone",
    "paper",
    "scissor"
]

while True:
    option = input("Enter your option (stone/paper/scissor): ").strip().lower()
    
    # Check if the input is valid
    if option in options:
        game = random.choice(options)
        print(f"Computer chose: {game}")
        
        if option == game:
            print("Match Draw...")
        elif (option == "stone" and game == "scissor") or \
             (option == "paper" and game == "stone") or \
             (option == "scissor" and game == "paper"):
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid option. Please choose stone, paper, or scissor.")
    
    exit_choice = input("Do you want to exit the match (yes/no)? ").strip().lower()
    if exit_choice == "yes":
        break

print("Thanks for playing with us!")
