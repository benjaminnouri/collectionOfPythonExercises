# Read input from the user
input_str = input()

# Strip whitespace and split the input into a list
positions = input_str.strip().split()

# Sort the positions to find the minimum and maximum
positions.sort()

# Calculate the minimum distance they need to travel to meet
low = (float(positions[1]) - float(positions[0])) + (float(positions[2]) - float(positions[1]))

# Convert to integer for output
rou = int(low)

# Check if the distance is an integer and print accordingly
if low / rou == 1: 
    print(rou)
else:
    print(low)



    

            













    


         

        
    
 



     



