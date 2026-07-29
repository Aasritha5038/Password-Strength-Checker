import re

print("=" * 40)
print("     PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter your password: ")

score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# Check uppercase letter
has_upper = False
for letter in password:
    if letter.isupper():
        has_upper = True

if has_upper:
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

# Check lowercase letter
has_lower = False
for letter in password:
    if letter.islower():
        has_lower = True

if has_lower:
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

# Check number
has_digit = False
for letter in password:
    if letter.isdigit():
        has_digit = True

if has_digit:
    score += 1
else:
    suggestions.append("Add at least one number.")

# Check special character
has_special = False
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

for letter in password:
    if letter in special_characters:
        has_special = True

if has_special:
    score += 1
else:
    suggestions.append("Add at least one special character.")

# Display result
print("\n" + "=" * 40)

if score <= 2:
    print("Password Strength : WEAK")
elif score <= 4:
    print("Password Strength : MEDIUM")
else:
    print("Password Strength : STRONG")

print("=" * 40)

# Display suggestions
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nExcellent! Your password is secure.")