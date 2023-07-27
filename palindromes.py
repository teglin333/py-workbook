def processString(func):
    def wrapper(raw_string):
        return func(''.join(e for e in raw_string if e.isalnum()))
    return wrapper
        
@processString
def testPalindrome(string: str) -> bool:
    """
    Test if the provided string is a palindrome.
    A string is a palindrome if it is identical forward and backward.
    """
    reverse: list = []
    
    for char in string:
        reverse.insert(0, char)
    if reverse == list(string):
        return True
    else:
        return False
    
print(testPalindrome("lev#$e  l"))      # True
print(testPalindrome("io9"))            # False