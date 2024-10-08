# Implementation Using Python Functions
# Read input string from the user
input_expression = input()

# Split the input string into numbers
numbers = input_expression.split('+')

# Sort the numbers
numbers.sort()

# Generate the output in the desired format
output_expression = '+'.join(numbers)

# Print the output
print(output_expression)



####################################################################################################
# Manual Implementation Without Using Built-in Methods
# Read input string from the user
input_str = input()

# Variables to hold counts of 1s, 2s, and 3s
ones = ""
twos = ""
threes = ""

# Process the input string manually
for i in range(0, len(input_str), 2):
    if input_str[i] == '1':
        ones += '1+'  # Append '1+' to the ones string
    elif input_str[i] == '2':
        twos += '2+'  # Append '2+' to the twos string
    elif input_str[i] == '3':
        threes += '3+'  # Append '3+' to the threes string

# Remove the last '+' from each string if they are not empty
if len(ones) > 0:
    ones = ones[:-1]
if len(twos) > 0:
    twos = twos[:-1]
if len(threes) > 0:
    threes = threes[:-1]

# Combine the final output
output = ones
if len(ones) > 0 and (len(twos) > 0 or len(threes) > 0):
    output += '+'  # Add '+' if ones are present and either twos or threes are present
output += twos
if len(twos) > 0 and len(threes) > 0:
    output += '+'  # Add '+' if both twos and threes are present
output += threes

# Print the final output
print(output)

        
  
   