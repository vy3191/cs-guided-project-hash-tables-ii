def printAnagramsTogether(words):
  grouped_words = {}	
	# Put all anagram words together in a dictionary 
	# where key is sorted word
  for word in words:
    sorted_word = "".join(sorted(word))
    # if grouped word in the grouped_words
    if sorted_word in grouped_words:
      grouped_words[sorted_word].append(word)
    else:
      grouped_words[sorted_word] = [word]  
    
  results = [ x[1] for x in grouped_words.items()]
  print(results)
     
	


arr = ["cat", "dog", "tac", "god", "act"] 
str1 = ["apt","pat","ear","tap","are","arm"]
printAnagramsTogether(arr)	
printAnagramsTogether(str1)	