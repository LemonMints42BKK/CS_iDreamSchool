password = "cupcake"
guess = ""
secret_message = 'Tomorrow, I will bring cookies for me and you to share at lunch!'

while guess != password:
    print("What is the password? ")
    guess = input()
print(f"Correct password! The secret message is: {secret_message}")