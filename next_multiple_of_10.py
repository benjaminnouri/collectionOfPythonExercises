# Read a number from input
var = int(input())

# Calculate the next multiple of 10 greater than the input number
next_multiple_of_10 = (var - (var % 10)) + 10

# Print the result
print(next_multiple_of_10)
