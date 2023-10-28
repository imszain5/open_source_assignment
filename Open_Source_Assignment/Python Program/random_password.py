import random
import string

def generate_random_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = random.choice(string.ascii_lowercase) + \
               random.choice(string.ascii_uppercase) + \
               random.choice(string.digits) + \
               random.choice(string.punctuation)

    password += ''.join(random.choice(characters) for _ in range(length - 4))

   
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

length = int(input("Enter the length of the random password: "))

if length < 4:
    print("Password length should be at least 4 characters.")
else:
    password = generate_random_password(length)
    print("Random Password:", password)
