with open("kagwi1.txt", "r") as file:
    data = file.read()
uppercase_data = data.upper()
with open("output22.txt", "w") as file:
    file.write(uppercase_data)

file = input("Enter the filename to read: ")
try:
    with open(filename, "r") as file:
        data = file.read()
        print(data)
    data = file.read()
except FileNotFoundError:
    print("File not found.")
print("File read successfully.")