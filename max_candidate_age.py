# Initialize the maximum age variable
max_age = 0  # To store the maximum age found
age = 0  # To temporarily store the input age

# Continue to read input until -1 is entered
while age != -1:
    age = int(input())  # Read age from input
    
    # Check if age is within the valid range (10 to 90)
    if 10 <= age <= 90:
        # Update max_age if the current age is greater
        if age > max_age:
            max_age = age

# Print the maximum age found
print(max_age)


