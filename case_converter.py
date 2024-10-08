# Read input string
input_str = input()

# Initialize counters for uppercase and lowercase letters
count_big = 0
count_small = 0

# Count the number of uppercase and lowercase letters
for char in input_str:
    if 'A' <= char <= 'Z':
        count_big += 1
    elif 'a' <= char <= 'z':
        count_small += 1

# Convert and print the string based on the counts
if count_big > count_small:
    print(input_str.upper())  # Convert to uppercase if there are more uppercase letters
else:
    print(input_str.lower())   # Convert to lowercase otherwise








    


         

        
    
 



     



