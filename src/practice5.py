# Given two strings a and b, determine if they are isomorphic.

# Two strings are isomorphic if the characters in a can be replaced to get b.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
def csIsomorphicStrings(a, b):
    # convert the string a into arr
    keys = list(a)
    # also conver the b into arr and use this one as value in the dict
    values = list(b)
    # if the lengths vary then return False
    if len(keys) != len(values):
        return False
    # now, have a iso_dict
    iso_dict = { }    
    # Now, loop through the array
    for i in range(len(a)):
        # if the char from either keys or values not in the dict
        if (keys[i], values[i]) not in iso_dict.items():
            # make sure the nothings exists in the keys
            if keys[i] in iso_dict.keys():
                return False
            if values[i] in iso_dict.values():
                return False
        iso_dict[keys[i]] = values[i]
        
    return True

print(csIsomorphicStrings(a = "odd",b = "egg"))
print(csIsomorphicStrings("foo", "bar"))
                        
        
           
        

