# ============================================================
#                   PASSWORD GENERATOR
#         Generates strong random passwords instantly
# ============================================================

import random

# Character sets
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers   = "0123456789"
symbols   = "@#$%&*-_"

# All characters combined
all_chars = lowercase + uppercase + numbers + symbols

# ── Welcome message ─────────────────────────────────────────
print("=" * 40)
print("       STRONG PASSWORD GENERATOR")
print("=" * 40)

# ── Main loop ───────────────────────────────────────────────
while True:
    print("\n  [1] Generate new password")
    print("  [2] Exit")

    choice = input("\n  Your choice: ").strip()

    # ── Generate password ───────────────────────────────────
    if choice == "1":

        # Get password length from user
        try:
            length = int(input("\n  How many characters? (min 6): "))

            if length < 6:
                print("\n  [!] Please enter at least 6 characters.")
                continue

        except ValueError:
            print("\n  [!] Please enter a valid number.")
            continue

        # Build the password character by character
        password = ""
        for i in range(length):
            character = random.choice(all_chars)
            password  = password + character

        # Display the generated password
        print("\n  ─────────────────────────────")
        print(f"  Password : {password}")
        print(f"  Length   : {length} characters")
        print("  ─────────────────────────────")

    # ── Exit ────────────────────────────────────────────────
    elif choice == "2":
        print("\n  Goodbye! Stay secure. 🔐")
        print("=" * 40)
        break

    # ── Invalid input ───────────────────────────────────────
    else:
        print("\n  [!] Invalid choice. Please type 1 or 2.")
