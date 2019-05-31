#function to check whether a string is pangram or not

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    
    str1_lower = str1.lower().replace(" ", "")
    alphabet_list = list(alphabet)
    new_list = []

    for letter in alphabet_list:
        if letter in str1_lower:
            new_list.append(letter)
    return len(new_list) == 26

