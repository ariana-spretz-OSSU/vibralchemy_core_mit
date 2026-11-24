def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements 
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError. 
    """ 
    length_total = 0
    for elem in L:
        if type(elem) == str:
            length_total += len(elem)
        elif type(elem) == list:
            for sub_elem in elem:
                if type(sub_elem) == str:
                    length_total += len(sub_elem)
                else:
                    raise ValueError
        else:
            raise ValueError
    return length_total
# Examples: 
print(sum_str_lengths(["abcd", ["e", "fg"]])) # Output: 7 
print(sum_str_lengths([12, ["e", "fg"]])) # raises ValueError 
print(sum_str_lengths(["abcd", [3, "fg"]])) # raises ValueError 