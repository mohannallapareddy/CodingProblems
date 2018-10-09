import numpy as np
from math import ceil

def readNumber():
        ###Function to input a number and reject any other data type
        number=input("Please enter a number n:")
        if number.isnumeric():
                return int(number)
        else:
                return int(readNumber())


def playGame():
        ###Code to play game
        n=readNumber()
        numlist=[0,n]
        codelist=['h','l','c']
        global numguess
        global guess
        numguess=0
        while True:
                guess=ceil(np.median(numlist))
                diff=numlist[1]-numlist[0]
                if diff == 2:
                        printDetails()
                code=input(guess)
                if code not in codelist:
                        print("The accepted values are h,l and c. Enter code again:")
                elif code == 'h':
                        numlist[1] = guess
                        numguess +=1
                        guess=ceil(np.median(numlist))
                elif code =='l':
                        numlist[0] = guess
                        numguess +=1
                        guess=ceil(np.median(numlist))
                elif code == 'c':
                        printDetails()


def printDetails():
        ###Fucntion to print the answer and number of guesses taken for each game
        global numguess
        global numgames
        numguess +=1
        print("Your number is",guess)
        numgames +=1
        guesslist.append(numguess)
        print("It took me",numguess,"guesses")
        print("I averaged %.2f"%(np.mean(guesslist)),"guesses per game for",numgames,"games(s)")
        if input("Play again (y/n)?") == 'y':
                playGame()
        else:
                #quit()
                exit(0)


#Declaring global variables and list to play the game
guesslist=[]
numgames=0
numguess=0
guess=0
print("In this game, you think of a number from 1 through n and I will try to guess what it is. After each guess, enter h if my guess is too high, l if too low, or c if correct.")

playGame()