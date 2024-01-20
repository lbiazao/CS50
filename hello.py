# Ask user for their name
name = input("What's your name? ")

# Remover whitespace from str and capitalize user's name 
name = name.strip().title()

# Say hello to user
print(f"Hello, {name}")