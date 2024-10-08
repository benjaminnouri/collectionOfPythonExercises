# Read the age from input
var = int(input())

# Check the age range and print the corresponding category
if var > 0 and var < 6:
    print("khordsal")
elif var >= 6 and var < 10:
    print("koodak")
elif var >= 10 and var < 14:
    print("nojavan")
elif var >= 14 and var < 24:
    print("javan")
elif var >= 24 and var < 40:
    print("bozorgsal")
else:
    print("miansal")


