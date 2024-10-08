# Initialize variables
total_points = 0  # Sum of total points
wins = 0  # Number of wins (games with 3 points)

# Loop to get input for 30 games
for _ in range(30):
    points = int(input())  # Get the points for the game
    total_points += points  # Add points to the total

    # Check if the game was a win
    if points == 3:
        wins += 1

# Print the total points and the number of wins
print(total_points, wins)






