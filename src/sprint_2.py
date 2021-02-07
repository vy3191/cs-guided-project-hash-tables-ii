# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
def first_not_repeating_character(s):
    # have char dictionary
    char_dict = {}
    # loop through the given stirng
    for char in s:
        # if char not in dict
        if char not in char_dict:
            # add to the dict with values as its frequency
            char_dict[char] = 1
        else:
            # if already there in the dict increament its frequency
            char_dict[char] += 1
    # Now loop through the dictionary            
    for item in char_dict.items(): 
        # check each items values
        # if item value is 1 then return the item's key
        if item[1] == 1:
            return item[0]
    # default return
    return '_'  
  
print(first_not_repeating_character('abacabad'))
print(first_not_repeating_character('abacabaabacaba'))