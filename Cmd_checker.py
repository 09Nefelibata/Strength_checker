import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    else:
        remarks += "❌ Password must be at least 8 characters long.\n"

    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks += "❌ Add lowercase letters.\n"

    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks += "❌ Add uppercase letters.\n"

    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks += "❌ Add numbers.\n"

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "❌ Add special characters.\n"

    if strength == 5:
        return "✅ Strong Password!"
    elif strength >= 3:
        return "⚠️ Moderate Password\n" + remarks
    else:
        return "❌ Weak Password\n" + remarks
print("🔐 Password Strength Checker")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter your password: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Exiting Password Strength Checker. Stay secure!")
        break

    result = check_password_strength(user_input)
    print(result)
    print("-" * 50)
