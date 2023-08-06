from os import system
from random import choice
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

def print_stage(lives_remaining):
    """Helper - prints the stage based on lives remaining"""
    print(stages[lives_remaining])

def clear():
    """Helper - clears the system console for better user experience"""
    _ = system('clear')

def encode_word(word_to_encode, optional_override_letter = "~"):
    """Encodes the word to be guessed into a character list with guess spaces"""
    encoded_word_response = []
    for char in word_to_encode:
        if "~" == optional_override_letter:
            encoded_word_response += char
        else:
            encoded_word_response += optional_override_letter
    return encoded_word_response

def get_letter_guess():
    """Helper - gets a letter guess from the player"""
    letter_guess = input("Guess letter: ")
    return letter_guess

def match_positions(encoded_word_to_match, letter_to_match):
    """Helper - identifies position(s) where letter matches encoded word"""
    position_response = []
    index = 0
    for letter in encoded_word_to_match:
        if letter_to_match == letter:
            position_response.append(index)

        index += 1
    return position_response

def main():
    """Let's play Hangman!!"""

    # Logo
    print(logo)

    # Choose the word 
    word = choice(word_list)
    encoded_word = encode_word(word)
    encoded_status = encode_word(word,"-")
    correctly_guessed_letters = 0

    # Outer loop
    lives = 7
    is_solved = False
    guesses = []
    while lives > 0 and not is_solved:

        # Get next guess
        guessed_letter = get_letter_guess()

        # Error check - make sure not a duplicate guess
        if guessed_letter in guesses:
            print(f"Letter: {guessed_letter} , has already been guessed!")
        else:
            guesses += guessed_letter

            # Check letter, remove from encoded word if applicable
            if guessed_letter in word:
                positions = match_positions(encoded_word,guessed_letter)
                correctly_guessed_letters += len(positions)
                for position in positions:
                    encoded_status[position] = guessed_letter
                print(f"{encoded_status}")
                if correctly_guessed_letters == len(word):
                    is_solved = True
            else:
                lives -= 1
                print_stage(lives)
    
    # Final resolution
    if is_solved:
        print(f"You solved it: {word}")
    else:
        print(f"HUNG - the word was {word}")

if __name__ == "__main__":
    main()