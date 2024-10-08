# Read a positive number from input
number = int(input())

# Check if the number is prime
if number > 1:
    is_prime = True  # Assume the number is prime initially
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")


