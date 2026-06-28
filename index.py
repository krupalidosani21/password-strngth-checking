import re
import random
import string

# List of common weak passwords
common_passwords = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "admin", "welcome", "letmein"
]

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_password(password):
    score = 0
    suggestions = []

    print("\n===== PASSWORD ANALYSIS =====")

    # Common password
    if password.lower() in common_passwords:
        print("❌ This is a commonly used password!")
        suggestions.append("Choose a unique password.")
    else:
        score += 20

    # Length
    if len(password) >= 8:
        print("✅ Good length")
        score += 20
    else:
        print("❌ Password should be at least 8 characters")
        suggestions.append("Increase password length.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        print("✅ Contains uppercase letter")
        score += 15
    else:
        print("❌ Missing uppercase letter")
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        print("✅ Contains lowercase letter")
        score += 15
    else:
        print("❌ Missing lowercase letter")
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        print("✅ Contains numbers")
        score += 15
    else:
        print("❌ Missing numbers")
        suggestions.append("Add numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("✅ Contains special characters")
        score += 15
    else:
        print("❌ Missing special characters")
        suggestions.append("Add special characters.")

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        print("⚠ Repeated characters detected")
        score -= 10
        suggestions.append("Avoid repeated characters.")

    # Sequential characters
    if "1234" in password or "abcd" in password.lower():
        print("⚠ Sequential pattern detected")
        score -= 10
        suggestions.append("Avoid predictable sequences.")

    # Prevent negative score
    score = max(0, score)

    # Strength
    if score < 40:
        strength = "Weak 🔴"
    elif score < 70:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    print("\nStrength:", strength)
    print("Score:", score, "/100")

    # Meter
    bars = score // 10
    print("Strength Meter: [" + "█" * bars + "-" * (10 - bars) + "]")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)

    if score < 70:
        print("\nSuggested Strong Password:")
        print(generate_password())


# Main
password = input("Enter your password: ")
check_password(password)
