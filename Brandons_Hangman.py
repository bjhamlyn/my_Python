import random
# The list of words that the game will choose from
words = ["python", "java", "computer", "computing", "ram", "linux", "cloud", "application"]

# This command randomly selects which word to use from teh list above
word = random.choice(words)

# This command writes underscores to serve as placeholders for the letters while the game is running
display = ["_"] * len(word)

# This command tracks how many guesses the player has used
wrong_guesses = 0

# This command lets the player continue to play until they either guess the correct word, or run out of guesses
while "_" in display and wrong_guesses < 6:
    print(" ".join(display))

    # This command prompts the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # The program then checks to see if the word contains the letter the player entered
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        # Tells the player the number of incorrect guesses
        wrong_guesses += 1

    # Display the hangman
    print("Hangman")
    if wrong_guesses == 1:
        print(" O")
    elif wrong_guesses == 2:
        print(" O")
        print(" |")
    elif wrong_guesses == 3:
        print(" O")
        print(" |")
        print("/|")
    elif wrong_guesses == 4:
        print(" O")
        print("/|\\")
    elif wrong_guesses == 5:
        print(" O")
        print("/|\\")
        print("/")
    elif wrong_guesses == 6:
        print(" O")
        print("/|\\")
        print("/ \\")

# This command determines whether the player won or lost
if "_" not in display:
    print("Congratulations! You won! The word was", word)
else:
    print("Sorry, you lost. Keep working on your vocabulary. The word was", word)
