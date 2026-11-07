############## YOU TRY IT ###################
# Write code that satisfies the following specification:
# your code here
def div_by(n, d):
    """ n and d are ints > 0. Returns True if d divides n evenly and False otherwise """
    if d % n == 0:
        return True
    else:
        return False

div_by(10, 3)
"""
Output:
True
"""        
div_by(195, 13)   
"""
Output:
False
"""
# For example: 
# print(div_by(10,3))     # print False
# print(div_by(195,13))   # returns True

##############################################

############## YOU TRY IT ###################
# Write code that satisfies the following specification:
# Hint, use paper and pen for a strategy before coding!
# your code here
def is_palindrome(s):
    """ s is a string
    Returns True if s is a palindrome and False otherwise
    """
    for char in range(len(s)):
        reverse = s[::-1]
        if s[char] == reverse[char]:
            return True
        else:
            return False
is_palindrome("hi")
"""
Output:
False
"""
is_palindrome("noon")
"""
Output:
True
"""
################################################
################################################
################ YOU TRY IT AT HOME #####################
################################################
# 1. Write code that satisfies the following specs:
# your code here
def keep_consonants(word):
    """ word is a string of lowercase letters
        Returns a string containing only the consonants 
        of word in the order they appear
    """
    new_string = ""
    for i in range(len(word)):
        vowels = "aeiou"
        if word[i] not in vowels:
            new_string += word[i]
    return new_string

keep_consonants("abcd")
"""
Output:
bcd
"""
keep_consonants("aaa")
"""
Output:
" "
"""
keep_consonants("babas")
"""
Output:
bbs
"""

# For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs
# 2. Write code that satisfies the following specs:
# your code here
def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    index_c = s.find(c)
    last_c = s.rfind(c)
    if c in s:
        return abs(index_c - last_c)
    else:
        return -1
        
first_to_last_diff("aaaa", "a")
"""
Output: 
3
"""
first_to_last_diff("abcabcabc", "b")
"""
Output: 
6
""" 
first_to_last_diff("abcabcabc", "d")
"""
Output: 
-1
"""
    
# For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('abcabcabc', 'd'))  # prints -1
################################################
################################################
################################################





