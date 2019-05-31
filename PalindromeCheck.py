#checks whether a passed in string is palindrome or not.

def palindrome(s):
    reverse = s[::-1]
    return s == reverse
