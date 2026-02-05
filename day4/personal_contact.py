contacts= {
    "kavya": 9876543210,
    "Bhoomika": 9123456780,
    "Meena": 9988776655
}
print(contacts)
contacts["gana"]=6787908990
print(contacts)
contacts.update({"gana" : 6363251490})
name = input("Enter name to search: ")

result = contacts.get(name, "Contact not found")
print(result)

for person, phone in contacts.items():
    print(f"Contact: {person} | Phone: {phone}")