def checkifpalindrome(s):
    return s == s[::-1]

s = "pawan"

print(checkifpalindrome(s))



# for case sensitive

def checkifpalindrome(s):
    s = s.lower()
    return s == s[::-1]



# Ignore spaces & special characters

import re

def checkifpalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(checkifpalindrome("A man, a plan, a canal: Panama"))



#Two Pointer Approach (DSA / Interview favorite)

def checkifpalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
