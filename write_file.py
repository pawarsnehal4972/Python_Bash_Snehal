# Task 3: Write to a File
# Creates a text file and writes some content to it.

file = open("sample_file.txt", "w")
file.write("Hello, this is my first file written with Python.\n")
file.write("Python makes file handling easy.\n")
file.write("This file was created for the Python and Bash assignment.\n")
file.close()

print("File 'sample_file.txt' created and content written successfully.")
