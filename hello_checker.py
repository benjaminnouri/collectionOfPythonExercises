# Read input string
input_string = input()

# Initialize variables to track the target string "hello"
target = "hello"
target_index = 0

# Loop through each character in the input string
for char in input_string:
    # Check if the current character matches the target character
    if char == target[target_index]:
        target_index += 1  # Move to the next character in "hello"
    # If we've matched all characters in "hello", we can stop
    if target_index == len(target):
        break

# Check if we matched all characters of "hello"
if target_index == len(target):
    print("YES")
else:
    print("NO")


        
    
 



     



