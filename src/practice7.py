# Given an array of strings strs, write a function that can group the anagrams. 
# The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def csGroupAnagrams(strs):
    # have hash table to store the given words
    group_dict = {}
    # loop through the given string
    for word in strs:
      uni = sum(ord(char) for char in word)
      if uni not in group_dict:
        group_dict[uni] = [word]
      group_dict[uni].append(word)
    print(group_dict)
    # have an empty array
    arr = [] 
    # loop through the grouped_dict
    for item in group_dict.items():
        arr.append(item[1])
    return arr       
  
strs = ["apt","pat","ear","tap","are","arm"]
print(csGroupAnagrams(strs))   
           