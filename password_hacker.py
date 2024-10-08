import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Clear the output file before writing
    with open(output_file_name, 'w', newline='') as Finr:
        Finr.write("")
    
    # Read input file and crack passwords
    with open(input_file_name) as Fin:
        reader = csv.reader(Fin)
        for row in reader:
            username = row[0]
            hashed_password = row[1]
            for i in range(1000, 10000):  # Check passwords from 1000 to 9999
                if hashlib.sha256(str(i).encode()).hexdigest() == hashed_password:
                    # Write the username and cracked password to the output file
                    with open(output_file_name, 'a', newline='') as Finw:
                        Finw.write(f"{username},{i}\n")
                    break  # Stop once the password is found


