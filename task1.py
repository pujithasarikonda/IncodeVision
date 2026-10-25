import string
import secrets


def generate_password(length):
    """Generate a strong random password."""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Ensure all required character types are included
    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Combine all character types
    all_characters = lowercase + uppercase + numbers + symbols

    # Generate remaining characters
    for _ in range(length - 4):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password_characters)

    return ''.join(password_characters)


def get_password_length():
    """Get a valid password length from the user."""

    while True:
        try:
            length = int(input("Enter the password length: "))

            if length < 4:
                print("Password length must be at least 4.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=" * 40)
    print("        PASSWORD GENERATOR")
    print("=" * 40)

    print("\nCreate a strong random password.")
    print("The password will contain:")
    print("- Uppercase letters")
    print("- Lowercase letters")
    print("- Numbers")
    print("- Symbols")

    print()

    length = get_password_length()

    password = generate_password(length)

    print("\n" + "=" * 40)
    print("Generated Password:")
    print("=" * 40)
    print(password)
    print("=" * 40)

    print("\nPassword generated successfully!")


if __name__ == "__main__":
    main()