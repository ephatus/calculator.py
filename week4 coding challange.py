with open('input.txt', 'w') as file:
    file.write('')  # Creates an empty file named newfile.txt
with open('input.txt', 'w') as file:
    file.write("kagwi is scu a greate guy and a good friend.\n")
    file.write("This is a new line added to the file.\n")
    file.write("God will for sure remember you kagwwi.\n ")
    file.write("kagwi remeber to depend on God always.\n")
    print("File updated successfully.")

    with open("input.txt", "r") as file:
        data = file.read()
    print(data)