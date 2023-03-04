import random

# Define the options
options = ["Rock", "Paper", "Scissors"]

# Define the game logic
def play(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Paper":
            return "You lose! Paper covers rock."
        else:
            return "You win! Rock smashes scissors."
    elif player == "Paper":
        if computer == "Scissors":
            return "You lose! Scissors cut paper."
        else:
            return "You win! Paper covers rock."
    elif player == "Scissors":
        if computer == "Rock":
            return "You lose! Rock smashes scissors."
        else:
            return "You win! Scissors cut paper."
    else:
        return "Invalid input! You have not entered Rock, Paper or Scissors."

# Define the main function to run the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")
    print(f"{player1_name} will be playing against {player2_name}.")
    print("The first player to win three rounds wins the game.")
    player1_score = 0
    player2_score = 0
    while True:
        print(f"\n{player1_name}'s Score: {player1_score}  |  {player2_name}'s Score: {player2_score}")
        player1_choice = input(f"{player1_name}, your turn: Rock, Paper, or Scissors? ").capitalize()
        while player1_choice not in options:
            player1_choice = input("Invalid input! Please enter Rock, Paper, or Scissors: ").capitalize()
        player2_choice = input(f"{player2_name}, your turn: Rock, Paper, or Scissors? ").capitalize()
        while player2_choice not in options:
            player2_choice = input("Invalid input! Please enter Rock, Paper, or Scissors: ").capitalize()
        result = play(player1_choice, player2_choice)
        print(f"\n{player1_name} chose {player1_choice}, {player2_name} chose {player2_choice}. {result}")
        if "win" in result:
            if result.startswith("You win"):
                player1_score += 1
            else:
                player2_score += 1
        if player1_score == 3:
            print(f"\nCongratulations, {player1_name}! You win the game!")
            break
        elif player2_score == 3:
            print(f"\nCongratulations, {player2_name}! You win the game!")
            break
    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == '__main__':
    main()
