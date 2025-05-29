import random

words = ['apple', 'banana', 'cherry', 'grapes', 'orange']
word_to_guess = random.choice(words)
guessed_word = ['_'] * len(word_to_guess)
guessed_letters = []
lives = 6

hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """
]

print("Welcome to Hangman!")
print("Guess the word. It has", len(word_to_guess), "letters.")

while lives > 0 and '_' in guessed_word:
    print(hangman_stages[6 - lives]) 
    print("Word: ", ' '.join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Lives remaining:", lives)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        print("Oops ! Wrong guess !")
        lives -= 1
if '_' not in guessed_word:
    print("\n Congratulations! You guessed the word:", word_to_guess)
else:
    print(hangman_stages[6 - lives])
    print("\n Game Over! The word was:", word_to_guess)
