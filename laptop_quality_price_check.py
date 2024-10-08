# Read the number of laptops
count = int(input())

# Initialize a list to store laptop data
laptops = []

# Read the price and quality of each laptop
for i in range(count):
    laptops.append(list(map(int, input().strip().split())))

# Check for the condition described by Irsa
found = False
for i in range(count):
    for j in range(count):
        if i != j:  # Ensure we're not comparing the same laptop
            price_i, quality_i = laptops[i]
            price_j, quality_j = laptops[j]
            if price_i < price_j and quality_i > quality_j:
                print("happy irsa")
                found = True
                break
    if found:
        break

if not found:
    print("poor irsa")

    


