"""
Created on Tue Nov 12 01:23:33 2024
@author: csesohag02
"""


#take random word and its length
from random_word import random_word
#take hangman stages
from hangman_stages import stages
#clear the  console screen
from subprocess import run

def play_game():
    word = random_word()
    blank = []
    guess_letters = []
    word_len = len(word)
    blank_char = word_len
    lives = 6
    
    for _ in range(word_len):
        blank.append('_')
    print(' '.join(blank))
    print(stages[lives])
    
    while True:
        if lives == 0:
            print("\nYou Lose!")
            break
    
        if blank_char == 0:
            print("\nYou Win!")
            break
    
        guess = input("\nGuess a letter: ").upper()
        if guess in guess_letters:
            print("You have already guessed this letter!")
            continue
        
        #clear the console
        run('cls', shell=True)
        
        guess_letters.append(guess)
        if guess in word:
            for i in range(word_len):
                if word[i] == guess:
                    blank[i] = guess
                    blank_char -= 1
        else:
            lives -= 1
            
        print(' '.join(blank))
        print(stages[lives])


play_game()
#play again
while True:
    ask = input("Do you want to play again?(Y/N): ").upper()
    if ask == 'N':
        print("See you next time!")
        break
    if ask == 'Y':
        run('cls', shell=True)
        play_game()
    else:
        print("Please enter valid choice!")
