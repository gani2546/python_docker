import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define the character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine all the selected character sets
    all_chars = lower_chars + upper_chars + digits + special_chars

    if not all_chars:
        raise ValueError("No characters available to generate a password.")

    # Ensure the password contains at least one of each selected character type
    password = [
        random.choice(lower_chars),
        random.choice(upper_chars) if include_uppercase else '',
        random.choice(digits) if include_numbers else '',
        random.choice(special_chars) if include_special_chars else ''
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
