contacts = []

while True:
    print("\n1. Add contact")
    print("2. View all")
    print("3. Search")
    print("4. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added.")
    elif choice == "2":
        for c in contacts:
            print(f"{c['name']} - {c['phone']}")
    elif choice == "3":
        search = input("Enter name to search: ")
        found = [c for c in contacts if search.lower() in c['name'].lower()]
        if found:
            for c in found:
                print(f"{c['name']} - {c['phone']}")
        else:
            print("Not found")
    elif choice == "4":
        break
    else:        
        print("Invalid choice")
        
        
# Exercise.
# Enhance the contact book: add delete by name, save to file (use open in write mode), load from file at start.

contacts = []

# Load from file
try:
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            contacts.append({"name": name, "phone": phone})
except FileNotFoundError:
    pass  # No saved file yet

while True:
    print("\n1. Add contact")
    print("2. View all")
    print("3. Search")
    print("4. Quit")
    print("5. Delete contact")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added.")
    elif choice == "2":
        for c in contacts:
            print(f"{c['name']} - {c['phone']}")
    elif choice == "3":
        search = input("Enter name to search: ")
        found = [c for c in contacts if search.lower() in c['name'].lower()]
        if found:
            for c in found:
                print(f"{c['name']} - {c['phone']}")
        else:
            print("Not found")
    elif choice == "4":
        break
    elif choice == "5":
        name = input("Enter name to delete: ")
        delete = [c for c in contacts if name.lower() in c['name'].lower()]
        if delete:
            contacts.remove(delete[0])
            print("Contact deleted.")
        else:
            print("Not found")
    else:        
        print("Invalid choice")
        
with open("contacts.txt", "w") as f:
    for c in contacts:
        f.write(f"{c['name']},{c['phone']}\n")