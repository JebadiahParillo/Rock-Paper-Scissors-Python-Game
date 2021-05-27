from random import randint

options = ["Rock", "Paper", "Scissors"]

computerplayer = options[randint(0, 2)]

userplayer = False

gamecount = 0

amountplayed = 0

retry = False

gamecount = int(input("Best of what would you like to play to\n"))

computerwincount = 0
playerwincount = 0


while userplayer == False:
    
    userplayer = input("Rock, Paper, Scissors? \n (You can also type r for rock p for paper or s for scissors\n")
    
    if userplayer == computerplayer:
        print("Tie")
    elif userplayer == "Rock" or userplayer == "r":
        if computerplayer == "Paper":
            print("You lost :(", computerplayer, "beats Rock")
            computerwincount = computerwincount+1
            amountplayed = amountplayed+1           
        else:
            print("You won :) Rock beats", computerplayer)
            playerwincount = playerwincount+1
            amountplayed = amountplayed+1
    elif userplayer == "Paper" or userplayer == "p":
        if computerplayer == "Scissors":
            print("You lost :(", computerplayer, "beats Paper")
            computerwincount = computerwincount+1
            amountplayed = amountplayed+1
        else:
            print("You won :) Paper beats", computerplayer)
            playerwincount = playerwincount+1            
            amountplayed = amountplayed+1            
    elif userplayer == "Scissors" or userplayer == "s":
        if computerplayer == "Paper":
            print("You lost :(", computerplayer, "beats Scissors")
            computerwincount = computerwincount+1
            amountplayed = amountplayed+1
        else:
            print("You won :) Scissors beats", computerplayer)
            playerwincount = playerwincount+1
            amountplayed = amountplayed+1            
    else:
        print("Try again I dont know what you want from me")
    
    if amountplayed > gamecount:
        if computerwincount > playerwincount:
            print("You lost :( computer:", computerwincount, "player", playerwincount)
            retry = input("Want to try again? Press y or n ")
            if retry == "y":
                gamecount = input("Best of what would you like to play to this time\n")
                userplayer = False
            else:
                userplayer = True
    else:
        if amountplayed < gamecount:
            userplayer = False
        else:
            print("You won :)  player:", playerwincount, "computer:", computerwincount)
            retry = input("Want to try again? Press y or n ")
            if retry == "y":
                gamecount = int(input("Best of what would you like to play to this time\n"))
                userplayer = False
            else:
                userplayer = True
    
    
    