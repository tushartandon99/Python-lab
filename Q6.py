contacts = {}

print("Commands: add, update, remove, search, show, exit")

while True:
    cmd = input("\nCommand: ").strip().lower()
    
    if cmd == 'add':
        name = input("Name: ").strip()
        contacts[name] = {"phone": input("Phone: ").strip(), "email": input("Email: ").strip()}
        print(f"Added {name}.")
        
    elif cmd == 'update':
        name = input("Name to update: ").strip()
        if name in contacts:
            contacts[name].update({"phone": input("New Phone: ").strip(), "email": input("New Email: ").strip()})
            print(f"Updated {name}.")
        else:
            print("Contact not found.")
            
    elif cmd == 'remove':
        name = input("Name to remove: ").strip()
        if contacts.pop(name, None):
            print(f"Removed {name}.")
        else:
            print("Contact not found.")
            
    elif cmd == 'search':
        q = input("Search value (name, phone, or email): ").strip()
        # List comprehension using .items() and .values() for dynamic lookup
        matches = [n for n, details in contacts.items() if q in n or q in details.values()]
        print(f"Matches found: {matches}")
        
    elif cmd == 'show':
        # Using .keys() and .values() explicitly
        print("All Contacts (Keys):", list(contacts.keys()))
        print("All Details (Values):", list(contacts.values()))
        
    elif cmd == 'exit':
        break
        
    else:
        print("Invalid command.")