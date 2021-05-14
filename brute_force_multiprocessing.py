import numpy as np
import multiprocessing as mp
import hashlib
import math
from sys import exit
import timeit

list_of_characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 
'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 
'E', 'R', 'T', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 
'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'0', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', 
'=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?',
 '/']

def try_password(hash_, password):
    pw_hash = string_to_hash_func(password)

    if hash_ == pw_hash:

        print(f"The password is: {password}")
        exit()
    else:
        pass

def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string


def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    # This is basically the code behind the itertools.combinations.
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

def try_all_possibilities(hash_, list_of_combinations, number_of_characters):
    x = len(list_of_combinations)

    z = 0

    while z < x:

        y = list_of_combinations[z]
        pw = []
        for i in y:
            pw.append(i)

        pw_join = ''.join(pw)
        print('.')
        try_password(hash_, pw_join)
       

        z += 1

def list_division(array_with_combinations):
    array = (np.array_split(array_with_combinations, mp.cpu_count()))

    return array


if __name__ == '__main__':

    hash_ = string_to_hash_func("//")

    number_of_characters = int(input("How many characters does the password have?"))

    y = list(combinations_with_replacement(list_of_characters, number_of_characters))

    print(y)

    arrays = list_division(y)

    queue = mp.Queue()

    for i in arrays:
        process = mp.Process(target=try_all_possibilities, args=(hash_, i, number_of_characters))
        process.start()
        