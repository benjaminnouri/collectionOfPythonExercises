from math import sqrt

# List to store the numbers
numbers = []
# String to store the final output
final_output = ""

# Read the count of numbers
count = int(input())
# Read each number and append it to the list
for i in range(count):
    numbers.append(float(input()))

# Calculate and print the square root for each number
for i in range(len(numbers)):
    # Format the square root to 8 decimal places
    formatted_str = str(format(float(sqrt(numbers[i])), '.8f'))
    # Build the output string with 4 decimal places
    for j in range(len(formatted_str) - 4):
        final_output += formatted_str[j]
    # Print the final output for the current number
    print(final_output)
    # Reset the final output for the next number
    final_output = ""
