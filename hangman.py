import os
import sys
import readline
from getpass import getpass


# TODO: make a list of correct guesses. if P2 guesses an already correct letter, the program shouts at them
# DISCLAIMER: i know i can refactor `letter_and_indices_to_replace` to be only one dimensional and have P2's guess be a single char, but it works this way so i'm keeping it. i know it's more confusing this way

def clear_screen():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():

    clear_screen()

    player_1_word = getpass("Player 1 enter word ").lower()
    player_1_word_stars = ["*" for i in range(len(player_1_word))]
    print(*player_1_word_stars)

    lives = 5
    letter_and_indices_to_replace = [[], []]
    incorrect_letters = []

    print("The program only accepts the first character of Player 2's input.")
    print("The program will only work with lowercase letters.")

    while True:
        try:
            if lives < 1:
                print(f"All lives lost. Word: {player_1_word}")
                break
            elif "".join(player_1_word_stars) == player_1_word:
                print(f"You win! Word: {player_1_word}")
                break

            player_2_guess = input("Player 2 enter guess ").lower()

            # accept only the first character of the input
            if player_2_guess[0] in player_1_word:
                print("Correct")

                letter_and_indices_to_replace[0].append(player_2_guess[0])  # put the guess itself into the first sub-list, ready to be processed

                # count the number of occurences of player_2_guess[0] in player_1_word
                for i in range(len(player_1_word)):
                    if player_2_guess[0] == player_1_word[i]:  # by iterating over P1's word, we get each index of P2's correct guess
                        letter_and_indices_to_replace[1].append(i)  # put the index of every occurrence of the P2's char in the second sub-list

                # replace characters in player_1_stars
                while len(letter_and_indices_to_replace[1]) != 0:

                    # the letter at the index (controlled by the first element of the second sublist) is reassigned the value of P2's guess
                    player_1_word_stars[letter_and_indices_to_replace[1][0]] = letter_and_indices_to_replace[0]

                    # this index is then removed from the list to not be processed again. we don't need it
                    letter_and_indices_to_replace[1].pop(0)
                print(*player_1_word_stars)

                # the 2d list is initialised, ready for the next guess
                letter_and_indices_to_replace = [[], []]
            else:
                incorrect_letters.append(player_2_guess[0])
                print("Incorrect. Incorrect letters: ", end='')
                print(*incorrect_letters)
                lives -= 1

        except IndexError or ValueError:
            print("Please enter a valid input.")


if __name__ == '__main__':
    main()
