# Initialize an empty list to store names
names_list = []

# Read 10 names from input
for i in range(10):
    name = input()
    # Standardize each name and append to the list
    names_list.append(name[0].upper() + name[1:].lower())

# Print the standardized names
for name in names_list:
    print(name)



        
  
   