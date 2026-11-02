# Task 4: Read from a File
# Opens the file in read mode and displays its content using read().

file = open("sample_file.txt", "r")
content = file.read()
file.close()

print("Content of sample_file.txt:")
print(content)
