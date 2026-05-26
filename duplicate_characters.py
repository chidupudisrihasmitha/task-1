#5 Remove Duplicate Characters from String

# Taking input from user
text = input("Enter a string: ")

# Removing duplicates
result = ""

for char in text:

    if char not in result:
        result = result + char

# Printing output
print("String after removing duplicates:", result)
