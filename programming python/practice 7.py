# --------------------------------------------------------
# Zenless Zone Zero Character Database
# Demonstrates lists, dictionaries, loops, and user input
# --------------------------------------------------------

# This list will store all characters as dictionary objects
characters = []

def add_character():
    name = input("Enter character name: ")
    faction = input("Enter faction: ")
    role = input("Enter combat role (e.g., attack, stun, support): ")

    # Each character is stored as a dictionary
    character = {
        "name": name,
        "faction": faction,
        "role": role
    }

    characters.append(character)
    print(f"[INFO] Character '{name}' added.\n")


def show_characters():
    if not characters:
        print("[INFO] No characters stored yet.\n")
        return

    print("\n=== STORED CHARACTERS ===")
    for id, char in enumerate(characters):
        print(f"{id + 1}. Name: {char['name']} | Faction: {char['faction']} | Role: {char['role']}")
    print()  # blank line


def edit_character():
    if not characters:
        print("[INFO] No characters to edit.\n")
        return

    show_characters()

    choice = input("Enter the number of the character you want to edit: ")

    # Validate input
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(characters):
        print("[ERROR] Invalid choice.\n")
        return

    index = int(choice) - 1
    char = characters[index]

    print(f"\nEditing '{char['name']}'... Leave blank to keep current value.")

    new_name = input(f"New name [{char['name']}]: ")
    new_faction = input(f"New faction [{char['faction']}]: ")
    new_role = input(f"New role [{char['role']}]: ")

    # Update only if user types something
    if new_name:
        char["name"] = new_name
    if new_faction:
        char["faction"] = new_faction
    if new_role:
        char["role"] = new_role

    print("[INFO] Character updated successfully.\n")


# ------------------ MAIN PROGRAM LOOP -------------------

while True:
    print("=== ZZZ Character Manager ===")
    print("1. Add Character")
    print("2. View Characters")
    print("3. Edit Character")
    print("4. Exit")
    
    user_choice = input("Choose an option (1-4): ")
    print()  # blank line

    if user_choice == "1":
        add_character()
    elif user_choice == "2":
        show_characters()
    elif user_choice == "3":
        edit_character()
    elif user_choice == "4":
        print("Exiting program. Goodbye.")
        break
    else:
        print("[ERROR] Invalid option. Please choose 1–4.\n")

