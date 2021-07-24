import random

#Making Roulette Wheel and assigning colors

def Play():
    num = random.randint(0, 36)
    print(f"The ball has landed on {num}({wheel[num]}).")
    return num, wheel[num]

def BettingonRed():
    bet = 1
    num, color = Play()
    if color == "Red":
        bet = bet + 1
        print("Congratulations! You win 1$.")
    else:
        bet = bet-1
        print("Game over! You lose.")
        
def BettingonaNumber():
    bet = 1
    player_num = int(input("Enter a number: "))
    num, color = Play()
    if player_num == num:
        bet = bet+35
        print("Congratulations! You win 35$.")
    else:
        bet = bet-1
        print("Game over! You lose.")
        
def MartinggaleSystem():
    winnings = 0
    bet = 1
    while True:
        num, color = Play()
        if color == "Red":
            bet = 1
            winnings = winnings + bet
            print("You win 1$!")
        else:
            bet = bet*2
            winnings = winnings - bet
            print(f"You lose. Your bet is now doubled to {bet}")
        if bet>100:
            print("Game over! You lose.")
            break
        if winnings >= 10:
            print("Congratulations! You win .")

def LabouchereSystem():
    lblist = []
    bet = 0 
    lblist_length = int(input("Enter number of elements: "))
    print("Enter the elements")
    for i in range(lblist_length):
        lblist.append(int(input()))
    while True:
        print("Your list is", lblist)
        if len(lblist)>1:
            bet = lblist[0]+lblist[-1]
        else:
            bet = lblist[0]
        if bet>100:
            print("Congratulations! You win.")
            break
        if not lblist:
            print("Game over! You lose.")
        num, color = Play()
        if color == "Red":
            print("You win!")
            lblist.append(bet)
            lblist.pop(0)
            lblist.pop(-1)
        else:
            lblist.append(bet)
def PlayGame():
    game = None
    while True:
        game = int(input("Welcome to Roulette! \n1. Betting on Red \n2. Betting on a Number \n3. Martingale System \n4. Labouchere System \n5. Exit \nEnter your choice: "))
        if game == 1: 
            BettingonRed()
        elif game == 2: 
            BettingonaNumber()
        elif game == 3: 
            MartinggaleSystem()
        elif game == 4: 
            LabouchereSystem()
        elif game == 5: 
            print("Thanks for playing!")
            break
        else: print("Invalid input! Please try again.")

wheel = {}
wheel[0] = "Green"
for i in range(37):
    if i in range(1,11) or range(19,29):
        if i%2 == 0: 
            wheel[i] = "Black"
        else:
            wheel[i] = "Red"
    else:
        if i%2 == 0: 
            wheel[i] = "Red"
        else:
            wheel[i] = "Black"

PlayGame()