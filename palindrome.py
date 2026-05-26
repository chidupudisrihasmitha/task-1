#3.palindrome


# Taking Input
num = input("Enter a number: ")


# Function
def check_palindrome(n):

    if n == n[::-1]:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")


# Function Call
check_palindrome(num)
