import random
import string
print(45*"-","PASSWORD GENERATOR",45*"-")
while True:
    try:
        pass_length = int(input("Enter the length of your password: "))
        if pass_length <= 0:
            print("Invalid Input.")
        else:
            break
    except ValueError:
        print("Invalid input.Enter integer value.")
char = string.ascii_letters
password = ''.join(random.choice(char)for i in range(0,pass_length))
print("\nGenerated Password:",password)
print("*"*110)
