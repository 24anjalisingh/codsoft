import random

def user_choice():
    choices = ["rock", "paper", "scissors"]
    user = input("Select one (rock, paper, scissors): ").lower()
    while user not in choices:
        user = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return user

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def result(user, computer, win):
    print(f"\nYou chose {user}, computer chose {computer}.\n")
    if win == "draw":
        print("It's a draw!")
    elif win == "player":
        print("You win!")
    else:
        print("You lose.")

def game():
    player_score = 0
    computer_score = 0

    while True:
        user = user_choice()
        comp = computer_choice()
        win = winner(user, comp)
        result(user, comp, win)

        if win == "player":
            player_score += 1
        elif win == "computer":
            computer_score += 1

        print(f"Scores -> You: {player_score}, Computer: {computer_score}")

        play_again = input("Want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    game()
