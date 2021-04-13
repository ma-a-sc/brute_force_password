import hashlib
from sys import argv

argy = hash_, hash_type, how_many_characters

def try_password():
    pass

def generate_password_length():
    x = how_many_characters
    y = 0
    password = []

    while y < x:
        password.append(0)
        y += 1

    return password

def generate_password():
    length = generate_password_length()

    for i in length:
        length[i] = list_of_characters_lowercase[1]

    print(length)


def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string


generate_password()



list_of_characters_lowercase:['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 
'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

list_of_characters_uppercase:['Q', 'W', 'E', 'R', 'T', 'U', 'I', 'O', 'P', 'A', 
'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

list_of_numbers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

list_of_symbols:['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
'_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',',
 '>', '.', '?', '/']

