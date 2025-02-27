import random

def password(length=8):
    upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_char = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    sym = "!@#$%^&*()-_=+?/>.<,"
    all_char = upp_char + low_char + num + sym
    
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None


    password = ''.join(random.choice(all_char) for i in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
password_result = password(password_length)

if password_result:
    print(f"Generated password: {password_result}")
