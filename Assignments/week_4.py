#Create a program that reads a file and write a modified version to a new file.

with open("maggy.txt", "r") as firstfile:
    content = firstfile.read()

# Modify to uppercase
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as secondfile:
    secondfile.write(modified_content)

print("The code works!!")

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except PermissionError:
    print(f"Error: You don’t have permission to read '{filename}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
