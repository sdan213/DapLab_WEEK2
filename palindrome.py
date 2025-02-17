#17. Create a function that checks if a passed string is a palindrome 
def is_palindrome(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]


print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
