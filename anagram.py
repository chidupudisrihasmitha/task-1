#2. Anagram


# Taking Input
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


# Function
def check_anagram(str1, str2):

    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")


# Function Call
check_anagram(word1, word2)


