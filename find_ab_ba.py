# Read input string
input_str = input()

# Convert the string to uppercase to handle case insensitivity
input_str = input_str.upper()

# Initialize flags for finding "AB" and "BA"
find_AB = False
find_BA = False

# Length of the input string
length = len(input_str)

# Check for "AB" and "BA" in the string without overlapping
for i in range(length - 1):
    if not find_AB and input_str[i:i+2] == 'AB':
        find_AB = True  # Found "AB"
        # Mark this pair as used by modifying the string
        input_str = input_str[:i] + 'NN' + input_str[i+2:]
    elif not find_BA and input_str[i:i+2] == 'BA':
        find_BA = True  # Found "BA"
        # Mark this pair as used by modifying the string
        input_str = input_str[:i] + 'NN' + input_str[i+2:]

# Check for the other pattern after marking
for i in range(length - 1):
    if find_AB and input_str[i:i+2] == 'BA':
        print("YES")  # Both "AB" and "BA" found
        break
    elif find_BA and input_str[i:i+2] == 'AB':
        print("YES")  # Both "AB" and "BA" found
        break
else:
    print("NO")  # Not found
