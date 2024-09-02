import string

def palindrome_dictionary(l):
  dict = {}
  new_line = ""
  
  for line in l:
    dict[line] = 0
    new_line = line.translate(str.maketrans('', '', string.punctuation))
    
    for word in new_line.split():
      word = word.lower()
  
      if word == word[::-1]:
        dict[line] += 1
        
  return dict

