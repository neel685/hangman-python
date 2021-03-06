import random
import time

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  ''')

print("Welcome to Hangman!\nBy Neel, Rohan & Tanya from 11F")
    
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main():
    choice1 = input("Do you want to choose your own set of words or want to play with programs default list of words [ own / default ] : ")
    choice1final = choice1.lower()
    if "own" in choice1final:
        hangman_own()
    elif "default" in choice1final:
        hangman_default()
    else:
        raise Exception("No such option. Please enter a valid choice by rerunning the program")
        return

def loadwords():
    global words_own_to_guess
    wordlist = input("Enter name of file(with extension .txt in the end) which contains the words: ")
    print("Loading words from ",wordlist)
    words = open(wordlist, 'r')
    wordsline = words.readline()
    words_own_to_guess = wordsline.split()
    print(len(words_own_to_guess)," words loaded.")
    return words_own_to_guess

def loadhints():
    global hintslist
    hintlist = input("Enter name of file(with extension .txt in the end) which contains the hints: ")
    print("Loading words from",hintlist)
    hints = open(hintlist, 'r')
    hintslines = hints.read()
    hintslist = hintslines.splitlines()
    print(len(hintslist),"hints loaded")
    return hintslist

def hangman_default():

    global word_to_guess
    words_to_guess = ["football","basketball","cricket","tennis","badminton"]
    word_to_guess = random.choice(words_to_guess)

    print("You must guess the word, you lose if you get 7 incorrect guesses.\nHint: Each of these words are sports.")
    
    wrong_guesses = 0
    displaylist = []

    for _ in range(len(word_to_guess)):
        displaylist.append("_ ")

    while wrong_guesses < 7:
        guess = input("Enter letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Only 1 letter input allowed, Please try again")
            continue
        elif guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if guess == word_to_guess[i]:
                    displaylist[i] = guess
                    guess_word = ''.join(displaylist)
                    print(guess_word)
                    if guess_word == word_to_guess:
                        print("Congratulations! You won!")
                        time.sleep(1)
                        return
                    else:
                        continue
                else:
                    continue
        else:
            print(HANGMANPICS[wrong_guesses])
            wrong_guesses += 1
            if wrong_guesses >= 5:
                hints_default(word_to_guess)
            else:
                continue
        
    print("you have 7 incorrect guesses, you lose! the word was", word_to_guess)

def hints_default(sport):
    sport = word_to_guess
    if sport == "football":
        print("Hint: It is team sport played with a spherical ball between two teams of 11 players.")
    elif sport == "basketball":
        print("Hint: It is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court.")
    elif sport == "cricket":
        print("Hint: It is a bat-and-ball game played between two teams of eleven players each on a field at the centre.")
    elif sport == "tennis":
        print("Hint: It is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles).")
    elif sport == "badminton":
        print("Hint: It is a racquet sport played using racquets to hit a shuttlecock across a net.")
    else:
        raise Exception("No such sport in words_to_guess.list")

def hangman_own():
    loadwords()
    loadhints()
    word_own_to_guess = random.choice(words_own_to_guess)
    word_index = int(words_own_to_guess.index(word_own_to_guess))

    print("You must guess the word, you lose if you get 7 incorrect guesses.")

    wrong_guesses = 0
    displaylist_own = []
    
    for _ in range(len(word_own_to_guess)):
        displaylist_own.append("_ ")

    while wrong_guesses < 7:
        guess = input("Enter letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Only 1 letter input allowed, Please try again")
            continue
        elif guess in word_own_to_guess:
            for i in range(len(word_own_to_guess)):
                if guess == word_own_to_guess[i]:
                    displaylist_own[i] = guess
                    guess_word = ''.join(displaylist_own)
                    print(guess_word)
                    if guess_word == word_own_to_guess:
                        print("Congratulations! You won!")
                        time.sleep(1)
                        return
                    else:
                        continue
                else:
                    continue
        else:
            print(HANGMANPICS[wrong_guesses])
            wrong_guesses += 1
            if wrong_guesses >= 5:
                print("Hint:",hintslist[word_index])
            else:
                continue
        
    print("you have 7 incorrect guesses, you lose! the word was", word_own_to_guess)

main()
