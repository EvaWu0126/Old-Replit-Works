from colorama import Fore, Back, Style
import random

def load_dictionary():
    return open("words.txt").readlines()

def get_word(words, length):
    # do the select matches algorithm to get a list of length-letter words
    matched = []
    for i in range(len(words)):
        words[i] = words[i].rstrip().upper()  # removes \n
        if len(words[i]) == length:
            matched.append(words[i])
    # return a random word from that matching list
    return (matched[random.randint(0, len(matched)-1)])

def count(letter, word):
    letterNum = 0
    for i in range(len(word)):
        if word[i] == letter:
            letterNum += 1

    return letterNum


def check_answer(guess, word):
    # return the colorful string indicating right and wrong
    result = ""
    for i in range(len(guess)):
        # right letter right place
        if guess[i] == word[i]:
            result += Back.GREEN + Style.DIM + Fore.BLACK + guess[i] +Style.RESET_ALL
            # remove the correct letter from the guess and the word
            guess = guess[0:i] + "*" + guess[i+1:]
            word = word[0:i] + "*" + word[i+1:]

        # right letter wrong place
        elif guess[i] in word and count(guess[i], guess[i:]) <= count(guess[i], word):
            result += Back.YELLOW + Fore.BLACK + guess[i] +Style.RESET_ALL
            guess = guess.replace(guess[i], "1", 1)

        # wrong letter
        else:
            result += Back.BLACK + Fore.WHITE + guess[i] +Style.RESET_ALL
    return result

def display_answers(guesses):
    for i in range(len(guesses)):
        print(guesses[i])


def wordle():
    words = load_dictionary()
    word = get_word(words, 5)
    guesses_left = 6
    guesses = []

    guess = input("Enter a 5 letter word: ")
    guesses_left -= 1
    while guess != word and guesses_left > 0:
        result = check_answer(guess, word)
        guesses += [result]
        display_answers(guesses)
        guesses_left -= 1
        guess = input("Enter a 5 letter word: ")

    if guess == word:
        print("You Won!")
    else:
        print("You lost. The word was " + word)

wordle()