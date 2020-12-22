# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Assignment 5, part 1
# Description:
# This program runs a word jumble game where a user tries to guess a word that is jumbled from a list
import random

def main():
    # original word list
    wordList = ['penguin', 'gorilla', 'kangaroo', 'lion', 'giraffe', 'elephant']

    # program chooses a word to be jumbled, turns it into a list, creates a list for jumbled letters
    word = random.choice(wordList)
    wordToList = list(word)
    jumbledList = []
    letterCounter = 0

    # fills in a new list to be turned into the jumbled word
    while letterCounter < len(word):
        randLetter = random.choice(wordToList)
        jumbledList.append(randLetter)
        wordToList.remove(randLetter)
        letterCounter += 1


    # turns the jumbled list into a string
    jumbledWord = "".join(jumbledList)
    # prints the jumbled word and prompts use to guess, initializes the counter at 1
    print("The jumbled word is \"" + jumbledWord + "\"\n")
    guess = input("Please enter your guess: ")
    counter = 1
    hint = "i"

    # prompts user to repeat guess if they don't get it right, and after two tries they will be asked if they want
    # a hint
    while guess != word:
        if counter >= 2:
            hint = input("Would you like a hint? (y/n): ")
            while hint != "Y" and hint != "y" and hint != "N" and hint != "n":
                hint = input("Please enter y or n: ")
            if hint == "y" or hint == "Y":
                if word == "penguin":
                    print("This animal is a bird that can't fly")
                elif word == "gorilla":
                    print("This animal is very big and hangs out in tropical forests")
                elif word == "kangaroo":
                    print("This animal loves to hop around")
                elif word == "lion":
                    print("This animal is often referred to as the king of the jungle")
                elif word == "giraffe":
                    print("This animal has a very long neck")
                elif word == "elephant":
                    print("This animal has a very long nose")
        print("Try again")
        counter += 1
        guess = input("Please enter your guess: ")
    # score based on number of attempts and if they used a hint
    score = 100 // counter

    if hint == "y" or hint == "Y":
        score = score // 2

    # prints out number of guesses and final score
    if guess == word and counter > 1:
        print("\nYou got it!\n\nIt took you", str(counter), "tries.")
        print("Your Score:", str(score) + "/100")
    if guess == word and counter == 1:
        print("\nYou got it!\n\nIt took you", str(counter), "try.")
        print("Your Score:", str(score) + "/100")


main()