
name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("marks.txt", "a") as file:
    file.write(f"{name} - {marks}\n")

print("Student marks appended successfully.")
