import random

# Step 1: Get user input for bounds
try:
    low = int(input("Enter lower bound: \n"))
    high = int(input("Enter high bound: \n"))
except ValueError:
    print("Please enter a valid number")

# Step 2: Generate random number within bounds
r = random.randint(low, high)

# Step 3: Set the guess count
guess_count = 5

# Step 4: Loop to handle guessing attempts
while guess_count > 0:
    try:
        new_guess_str = input(f"remained guess: {guess_count} => Enter your next guess: \n")
        new_guess = int(new_guess_str)
    except ValueError:
        print("Please enter a valid number")
        continue

    if r == new_guess:
        print("Great! Your guess is correct!")
        break
    elif r > new_guess:
        print("Your guess is lower than the selected number.")
    else:
        print("Your guess is higher than the selected number.")

    guess_count -= 1

if guess_count == 0:
    print(f"Sorry, you've run out of guesses. The correct number was {r}.")
