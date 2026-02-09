try:
    file=open("sample.txt" , "r")
    print(file.read())
except FileNotFoundError:
    print("File not found, Pls open existing file")
finally:
    file.close()