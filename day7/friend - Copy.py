
with open("friend.txt", "w") as file:
    for i in range(3):
        name = input(f"Enter friend {i+1} name: ")
        file.write(name + "\n")

print("Friend names saved successfully.")
