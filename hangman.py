import os
from getpass import getpass

# TODO: make a list of correct guesses. if P2 guesses an already correct letter, the program shouts at them

def main():

    os.system("clear")

    player_1_word = getpass("Player 1 enter word ").lower()
    player_1_word_stars = ["*" for i in range(len(player_1_word))]
    print(*player_1_word_stars)

    lives = 5
    letter_and_indices_to_replace = [[], []]
    incorrect_letters = []

    while True:
        try:
            if lives < 1:
                print(f"All lives lost. Word: {player_1_word}")
                break
            elif "".join(player_1_word_stars) == player_1_word:
                print(f"You win! Word: {player_1_word}")
                break
            player_2_guess = input("Player 2 enter guess ").lower()
            if player_2_guess[0] in player_1_word:
                print("Correct")
                letter_and_indices_to_replace[0].append(player_2_guess[0])
                # count the number of occurences of player_2_guess[0] in player_1_word
                for i in range(len(player_1_word)):
                    if player_2_guess[0] == player_1_word[i]:
                        letter_and_indices_to_replace[1].append(i)

                # replace characters in player_1_stars
                while len(letter_and_indices_to_replace[1]) != 0:
                    # letter_and_indices_to_replace[1] holds all the indices of characters to replace with the letter in [0][0]
                    # after the letter is replaced, it's removed
                    # this happens until the list is empty
                    player_1_word_stars[letter_and_indices_to_replace[1][0]] = letter_and_indices_to_replace[0][0]
                    letter_and_indices_to_replace[1].pop(0)
                print(*player_1_word_stars)

                letter_and_indices_to_replace = [[], []]
            else:
                incorrect_letters.append(player_2_guess[0])
                print(f"Incorrect. Incorrect letters: {incorrect_letters}")
                lives -= 1

        except IndexError or ValueError:
            print("please enter a valid input")


if __name__ == '__main__':
    main()

