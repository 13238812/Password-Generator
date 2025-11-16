import secrets

def generate_password(length, use_lowercase=True, use_uppercase=True, use_numbers=True, use_special=True):
    # Characters sets defined
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Selected characters are placed into a pool to be selected randomly
    characters = ""
    if use_lowercase:
        characters += lowercase
    if use_uppercase:
        characters += uppercase
    if use_numbers:
        characters += digits
    if use_special:
        characters += special

    # Error handling to prevent user from selecting no characters
    if not characters:
        raise ValueError("You must select at least one character type!")

    # Generate the characters and combine them
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")

    # Get password length and handle negative length errors
    while True:
        try:
            length = int(input("Enter password length (e.g., 12): "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    # Character type options
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    #Final results of user selections - generates the final password - Generates the value error in the event that no characters are selected
    try:
        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special)
        print("\nGenerated Password:", password)
    except ValueError as e:
        print("\nError:", e)

# Allows for modular use in the case that the code is imported
if __name__ == "__main__":
    main()