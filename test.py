import hashlib
import math

list_of_characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 
'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 
'E', 'R', 'T', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 
'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'0', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', 
'=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?',
 '/']

def try_password():
    pass

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    # the code behind the itertools.combinations
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

def possibilities(len_list, how_many_positions):
    x = pow(how_many_positions, len_list)

    return x


def replace_quotes(list_of_combinations):
    x = len(list_of_combinations)

    z = x - 1

    print(x)

    while z > 0:

        y = list_of_combinations[z]

        print(y)

        z -= 1


y = list(combinations_with_replacement(list_of_characters, 2))

replace_quotes(y)

    

def generate_password_length(user_def):
    x = user_def
    y = 0
    password = []

    while y < x:
        password.append("x")
        y += 1

    return password




def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string





