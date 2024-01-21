# Ask user for their name, remove spaces and capitalize the name input
name = input("What's your name? ").strip().title()

# Split full name into first and last name.
firstname, lastname = name.split(' ')

# Say hello to user
print(f"Hello, {firstname}")