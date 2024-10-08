# Initialize the maximum and second maximum variables
max_age = 0  # To store the largest age
second_max_age = 0  # To store the second largest age

# Start reading the ages from input
while True:
    age = int(input())  # Read the age
    
    if age == -1:  # Break the loop when -1 is entered
        break
    
    # Check if the age is within the valid range (10 to 90)
    if 10 <= age <= 90:
        # Update max_age and second_max_age accordingly
        if age > max_age:
            second_max_age = max_age
            max_age = age
        elif age > second_max_age:
            second_max_age = age

# Output the largest and second largest ages
print(f"{max_age} {second_max_age}")


   