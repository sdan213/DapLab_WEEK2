#18. Write a Python program to check if a passed string is a pangram or not.
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


print(is_pangram("The quick brown fox jumps over the lazy dog"))  
print(is_pangram("Hello world"))  
