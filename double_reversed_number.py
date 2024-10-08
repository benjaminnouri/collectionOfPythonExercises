# Read a three-digit number from input
var = int(input())

# Reverse the number by extracting digits and concatenate them as a string
reversed_num = int(str(var % 10) + str((var % 100) // 10) + str(var // 100))

# Print double the reversed number
print(reversed_num * 2)

