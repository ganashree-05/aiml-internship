import csv
with open("C:\\Users\\cngan\\Downloads\\Company_Data.csv",mode="r") as file:
    csv_file=csv.reader(file)
    for lines in csv_file:
        print(lines)
    