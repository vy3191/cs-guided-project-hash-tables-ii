# Given a pattern and a string a, find if a follows the same pattern.

# Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in s.

def csWordPattern(pattern, a):
    # have words dict
    list2 = a.split(" ")
    set1 = set()
    for char in pattern:
        set1.add(char)
    set2 = set()
    for word in list2:
        set2.add(word)
    # set2.add(list2)
    if len(set1) == len(set2):
        return True
    return False    
    
pattern = "abba"
a = "lambda school school lambda"
print(csWordPattern(pattern, a))

pattern1 = "abba"
a1 = "lambda school school coding"
print(csWordPattern(pattern1, a1))

pattern2 = "aaaa"
a2 = "lambda school school lambda"
print(csWordPattern(pattern2, a2))

