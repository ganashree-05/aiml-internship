filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
