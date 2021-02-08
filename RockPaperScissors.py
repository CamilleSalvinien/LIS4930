from random import randint

def letsPlay (times):
    humanWins = 0
    computerWins = 0
    for i in range(times):

        #set up the human choice
        print("This is the "+str(i+1)+" round!")
        print("Please choose between rock, paper, lizard, scissors and spock! And see if you can beat the game:")
        human = str(input())

        #set up the computer choice
        possibilities = ["rock","paper","lizard", "scissors", "spock"]
        computer = possibilities[randint(0,4)]

        print("1,2,3, say shoot... The computer choose "+str(computer)+".")

        #if human ties with computer
        if human == computer:
            print("You both tied!")
            if i == 0:
                i = 0
            else:
                i -=1

        #human is a rock
        elif human == "rock":
            if computer == "paper":
                print("You have been compressed... Computer wins!")
                computerWins+=1
            elif computer == "lizard":
                print("You crushed the computer... You win!")
                humanWins+=1
            elif computer == "scissors":
                print("You crushed the computer... You win!")
                humanWins+=1
            elif computer == "spock":
                print("You have been vapourised... Computer wins!")
                computerWins+=1

        #human is paper  
        elif human == "paper":
            if computer == "rock":
                print("You cover the computer... You win!")
                humanWins+=1
            elif computer == "lizard":
                print("The computer eats you... Computer wins!")
                computerWins+=1
            elif computer == "scissors":
                print("The computer cuts you... Computer wins!")
                computerWins+=1           
            elif computer == "spock":
                print("You disprove the computer... You win!")
                humanWins+=1
    
        #human is a lizard
        elif human == "lizard":
            if computer == "paper":
                print("You eat the computer... You win!")
                humanWins+=1
            elif computer == "rock":
                print("The computer crushes you... Computer wins!")
                computerWins+=1
            elif computer == "scissors":
                print("The computer decapitates you... Computer wins!")
                computerWins+=1      
            elif computer == "spock":
                print("You poison the computer... You win!")
                humanWins+=1

        #human in a scissor
        elif human == "scissors":
            if computer == "paper":
                print("You cut the computer... You win!")
                humanWins+=1
            elif computer == "lizard":
                print("You decapitate the computer... You win!")
                humanWins+=1
            elif computer == "rock":
                print("The computer crushes you... Computer wins!")
                computerWins+=1
            elif computer == "spock":
                print("The computer smashes you... Computer wins!")
                computerWins+=1

        #human is a spock
        elif human == "spock":
            if computer == "paper":
                print("The computer dispoves of you... Computer wins!")
                computerWins+=1
            elif computer == "lizard":
                print("The computer poisons you... Computer wins!")
                computerWins+=1
            elif computer == "scissors":
                print("You smash the computer... You win!")
                humanWins+=1
            elif computer == "rock":
                print("You vapoursied the computer... You win!")
                humanWins+=1

        #human didn't choose correclty        
        else:
            print("Please make sure to choose between: rock, paper, scissors, spock :)")
            if i == 0:
                i = 0
            else:
                i -=1

    if computerWins >= humanWins:
        print("The computer wins "+str(computerWins)+" to "+ str(humanWins)+". Better luck next time!")
    else:
        print("You have won! Congratulions!")

def plays():
    print("How many times would you like to play today?")
    times = int(input())
    return times


letsPlay(plays())
