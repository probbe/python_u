#calculates the number of upper case letters and lower case letters

def up_low(s):
    up_char = 0
    low_char = 0
    other_char = 0
    for letter in s:
        if letter.isupper():
            up_char = up_char +1
        elif letter.islower():
            low_char = low_char +1
        else:
            other_char = other_char +1
    print(f'No. of Upper case characters : {up_char}\nNo. of Lower case Characters : {low_char}\nNo. of other Characters : {other_char}')
