import random
import os
from hangman_art import stages, logo
from hangman_word import word_list

print(logo)
randomword = random.choice(word_list)
#print(f"The word is {randomword}")
disp = []
for i in randomword:
    disp.append("_")
print(disp)
lives = 6
over = 0
gl = []
while over == 0:
    guess = input("Enter guess: ").lower()
    os.system("clear")
    if guess not in gl:
        gl.append(guess)
    if guess in disp:
        print(f"You already guessed {guess}")
    for i in range(len(randomword)):
        ch = randomword[i]
        if guess == ch:
            disp[i] = guess
            print(f"{guess} is correct")
            print(f"{lives} lives remaining")
    print(f"Letters guessed till now: {gl}")

    if guess not in randomword:
        lives -= 1
        print(
            f"{guess} is not part of the word!\nLife Lost! \n{lives} lives remaining.")
        if lives == 0:
            print('\033[1m' + 'Press F to pay respect' + '\033[0m')
            f = input()
            print(f"You lose! \nThe word was {randomword}")
            over = 1
    print(f"{' '.join(disp)}")
    if "_" not in disp:
        print("You Win! GG")
        over = 1
    print(stages[lives])
