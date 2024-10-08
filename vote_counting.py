from collections import OrderedDict

# Read the total number of votes
count = int(input())

# Initialize an OrderedDict to store votes for each country
votes = OrderedDict()

# Count votes for each country
for _ in range(count):
    country = input().strip()
    votes[country] = votes.get(country, 0) + 1

# Sort the countries alphabetically and print the results
for country in sorted(votes.keys()):
    print(country, votes[country])
