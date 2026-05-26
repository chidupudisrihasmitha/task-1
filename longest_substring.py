# longest sub string

# Longest Substring Program

string = input("Enter string: ")

temp = ""
answer = ""

for char in string:

    if char not in temp:
        temp += char

    else:
        temp = temp[temp.index(char) + 1:] + char

    if len(temp) > len(answer):
        answer = temp


print("Longest substring:", answer)
print("Length:", len(answer))

