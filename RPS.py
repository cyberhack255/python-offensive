print("Welcome")
player1Name = input("Player 1 name: ")
player2Name = input("Player 2 name: ")

correctAnswers = ['rock', 'paper', 'scissors']

player1Score = 0
player2Score = 0

for game in range(3):
    print ("Game", game +1)
    player1Move = ''
    while player1Move not in correctAnswers:
        player1Move = input(player1Name + ", choose rock, paper or scissors: ")

    player2Move = ''
    while player2Move not in correctAnswers:
        player2Move = input(player2Name + ", choose rock, paper or scissors: ")

#Input choices from players
    print("Player 1 chose:", player1Move)
    print("Player 2 chose:", player2Move)

    if player1Move == player2Move:
        print("It's a tie!")
    elif (player1Move == 'rock' and player2Move == 'scissors') or (player1Move == 'paper' and player2Move == 'rock') or (player1Move == 'scissors' and player2Move == 'paper'):
        print(player1Name + " wins!")
        player1Score +=1
    else:
        print(player2Name + " wins!")
        player2Score +=1
#Display score
    print("Score:")
    print(player1Name + ":", player1Score)
    print(player2Name + ":", player2Score)

print("Final score:")
print(player1Name + ":", player1Score)
print(player2Name + ":", player2Score)
if player1Score > player2Score:
    print(player1Name + " wins!")
elif player1Score < player2Score:
    print(player2Name + " wins!")
else:
    print("It's a tie!")

print("Thank you for playing")