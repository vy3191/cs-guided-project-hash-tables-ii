# Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def csGroupAnagrams(strs):
    # have hash table to store the given words
    group_dict = {}
    # store all the words in the dict
    # where key is sorted word and values are all the related anagrams
    for word in strs:
        # now sort the each word
        sorted_word = "".join(sorted(word))
        # if the sorted word is not in the group dict, then place it as key: [word]
        if sorted_word not in group_dict:
            group_dict[sorted_word] = [word]
        else:
            group_dict[sorted_word].append(word)  
    
    # have an empty array
    arr = [] 
    # loop through the grouped_dict
    for item in group_dict.items():
        arr.append(item[1])
    return arr       
  
strs = ["apt","pat","ear","tap","are","arm"]
print(csGroupAnagrams(strs))   
           