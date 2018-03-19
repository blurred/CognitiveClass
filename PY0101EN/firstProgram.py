with open("fruits.txt", "r") as File1:
    file_content = File1.read()
    print(file_content)
print(File1.closed)
print(file_content)