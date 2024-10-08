import random

# 1) list of names
names = ['Hasan', 'Ali', 'Behnam', 'Mahmoud', 'Vahid', 'Amin']

# 2) select one name randomly
selected_name = random.choice(names)

guess_count = len(selected_name)
guessed_list = ['_'] * len(selected_name)

# 5) guess > 0 -> win/loss
while guess_count > 0:
    # Print current state
    print(' '.join(guessed_list))
    print(f'Remaining guesses: {guess_count}')
    
    # 3) get user char
    guessed_char = input('Enter a char: ').lower()
    
    # 4) check -> show feedback
    if guessed_char.isalpha():
        if guessed_char in selected_name.lower():
            if guessed_char in [char.lower() for char in guessed_list]:
                print("You have guessed this character before.")
            else:
                for idx, char in enumerate(selected_name.lower()):
                    if char == guessed_char:
                        guessed_list[idx] = selected_name[idx]
                print("Correct guess!")
        else:
            guess_count -= 1
            print(f'Wrong guess!')
    else:
        print("Please enter a valid character.")
    
    # Check for win condition
    if '_' not in guessed_list:
        print(f'Congratulations! You guessed the name: {selected_name}')
        break

# Check for loss condition
if guess_count == 0:
    print(f'Sorry, you ran out of guesses. The name was: {selected_name}')