#1 strong numbers


# Function to check Strong Number
def strong_number(num):

    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + fact[digit]
        temp = temp // 10

    if total == num:
        print(num, "is a Strong Number")
    else:
        print(num, "is not a Strong Number")


# Taking input
number = int(input("Enter a number: "))

# Function call
strong_number(number)
