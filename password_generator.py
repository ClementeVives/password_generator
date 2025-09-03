# import the random module to pick random elements
import random  

# Define the pool of characters the password can use
pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

password = ""  # start with an empty string to build the password

# Ask the user for the desired password length and convert it to an integer
length = int(input("How long should the password be? "))

# Loop 'length' times to build the password character by character
for _ in range(length):
    password += random.choice(pool)  # pick a random character and append to 'password'

# Print the final password
print("Password:", password)
