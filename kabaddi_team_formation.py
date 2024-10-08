# Read the number of players
count = int(input())

# Initialize a counter for valid players
count_team = 0

# Read the number of competitions each player has participated in
players = input().strip().split()

# Count players who can participate in the team
for i in range(len(players)):
    if int(players[i]) <= 2:
        count_team += 1

# Calculate the number of teams that can be formed
count_team = count_team // 3

# Print the result
print(count_team)




    

            













    


         

        
    
 



     



