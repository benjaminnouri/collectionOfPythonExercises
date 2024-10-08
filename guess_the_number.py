# Set the initial range for guessing
low = 1
high = 99

# Start the guessing loop
while True:
    # Guess the middle number between low and high
    guess = (low + high) // 2
    print(f"My guess is: {guess}")

    # Ask the user for feedback
    feedback = input("Is your number (k: smaller, b: bigger, d: correct)? ").lower()

    # Process user feedback
    if feedback == 'd':
        print("Yay! I guessed it!")
        break
    elif feedback == 'k':
        # The number is smaller than the guess, adjust the high range
        high = guess - 1
    elif feedback == 'b':
        # The number is bigger than the guess, adjust the low range
        low = guess + 1
    else:
        print("Invalid input, please enter 'k', 'b', or 'd'.")

