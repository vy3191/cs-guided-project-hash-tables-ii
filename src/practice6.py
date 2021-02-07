# Given two strings a and b, determine if they are isomorphic.

# Two strings are isomorphic if the characters in a can be replaced to get b.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
def csIsomorphicStrings(a, b):
    # convert the string a into arr
    if len(a) != len(b):
      return False
    # create sets for both string a and string b
    str_a = set(a)
    str_b = set(b)
    # comparing its lengths, if one is larger then the other, 
    # then characters are not being repeated isomorphically
    if len(str_a) != len(str_b):
      return False
    
    return True
    

print(csIsomorphicStrings(a = "odd",b = "egg"))
print(csIsomorphicStrings("foo", "bar"))
                        
        
           
        

