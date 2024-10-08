# Read input string
input_str = input()

# Convert the string to lowercase to ignore case
input_str = input_str.lower()

# Determine the length of the string and calculate the midpoint
length = len(input_str)
midpoint = length // 2

# Initialize lists to hold the first half and the reversed second half of the string
list_part1 = []
list_part2 = []

# Fill the first half of the string
for i in range(midpoint):
    list_part1.append(input_str[i])

# Fill the reversed second half of the string
for i in range(-1, -(midpoint + 1), -1):
    list_part2.append(input_str[i])

# Check if the two halves are equal
is_palindrome = True
for i in range(midpoint):
    if list_part1[i] != list_part2[i]:
        is_palindrome = False
        break

# Print the result
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")












    


         

        
    
 



     



