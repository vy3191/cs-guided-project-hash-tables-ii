"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
def frequency_sort(s: str) -> str:
    # Your code here
    letter_dict = {}
    for char in s:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1   
    # print(letter_dict)   
    sorted_letters = sorted(list(letter_dict.items()), key=lambda item: item[1], reverse=True) 
    # print(sorted_letters)  
    new_str=""
    for tup in sorted_letters:
        new_str += tup[0]*tup[1]
    print(new_str)
           
    
results1= frequency_sort("free")     # "eefr"
results2 = frequency_sort("dddbbb")   # "dddbbb"
results3 = frequency_sort("Bbcc")   # "ccBb"
print(results1)

    