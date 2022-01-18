import random
import time

def hangman():
    
    wrong_guesses = 0
    displaylist = []
    
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

    for _ in range(len(word_to_guess)):
        displaylist.append("_ ")

    while wrong_guesses < 7:
        guess = input("Enter letter: ")
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
                hints(word_to_guess)
            else:
                continue
        
    print("you have 7 incorrect guesses, you lose! the word was", word_to_guess)

def hints(sport):
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
    
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  ''')

print("Welcome to Hangman!\nBy Neel, Rohan & Tanya from 11F")

words_to_guess = ["football","basketball","cricket","tennis","badminton"]
word_to_guess = random.choice(words_to_guess)

print("You must guess the word, you lose if you get 7 incorrect guesses.\nHint: Each of these words are sports.")

hangman()
