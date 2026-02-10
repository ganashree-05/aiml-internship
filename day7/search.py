
search_name = input("Enter name to search: ")
found = False

with open("friend.txt", "r") as file:
    for line in file:
        if search_name.lower() == line.strip().lower():
            found = True
            break

if found:
    print("Found")
else:
    print("Not Found")
