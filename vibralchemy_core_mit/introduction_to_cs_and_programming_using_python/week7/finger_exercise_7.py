def div_by(n, d):
    """ n and d are ints > 0. Returns True if d divides n evenly and False otherwise """
    if d % n == 0:
        return True
    else:
        return False
        
div_by(195, 13)   

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

keep_consonants("abracadabra")


def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    index_c = s.index["c"]
    last_c = s.rindex["c"]
    if c in s:
        return index_c - last_c
    else:
        return -1
        
first_to_last_diff("aaaa", "a")

