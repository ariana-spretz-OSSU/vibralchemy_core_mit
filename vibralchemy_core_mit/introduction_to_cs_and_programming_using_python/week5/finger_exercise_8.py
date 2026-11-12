def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and viceversa. 
    If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here     
    
    equal = ""
    not_equal = ""
    for i in range(0, len(s1)):
        if s1[i] not in equal: 
            equal += s1[i]
        if s1[i] not in s2:
            not_equal += s1[i]
            
    for j in range(0, len(s2)):
        if s2[j] not in equal or s2[j] not in s1: 
            not_equal += s2[j]
            
    if not_equal == "":
        return True
    else:
        return False
        
# Examples: 
print(same_chars("abc", "cab")) 
# Output True 
print(same_chars("abccc", "caaab")) 
# Output True 
print(same_chars("abcd", "cabaa")) 
# Output False 
print(same_chars("abcabc", "cabz")) 
# Output False 