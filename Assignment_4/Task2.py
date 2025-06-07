info = input("Enter text to write to the file: ")
with open('Assignment_4/output.txt', 'w') as file:
    file.write(info + '\n')

with open('Assignment_4/output.txt', 'a') as file:
    file.write(input("Enter additional text to write to file: "))

with open('Assignment_4/output.txt', 'r') as file:
    data = file.read()
    print("File content of file output.txt:")
    print(data)