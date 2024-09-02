def magical_words(word_list):
    
  # Find the Word with the Most Vowels
  vowels_count = []
  for word in word_list:
    count = 0
    for char in word:
      if(char.lower() in "aeiou"):
        count += 1
    
    vowels_count.append((count, word))
    vowels_count.sort()
    
  max_count = 0
  for count, word in vowels_count:
      if max_count < count:
          max_count = count

  for count, word in vowels_count:
      if count == max_count and word.isupper():
          print("Highest Vowels:",word)
          break
      elif count == max_count:
          print("Highest Vowels:",word)
          break
        
        
  # Identify Palindrome Words
  palindrome_word_list = []
  for word in word_list:
    if word.lower() == word[::-1].lower():
      palindrome_word_list.append(word)
  
  # Print the palindromes as a comma-separated list
  if palindrome_word_list:
      print("Palindrome:", ", ".join(palindrome_word_list))
  else:
      print("Palindrome: None")
    
  # Count Duplicate Word
  duplicate_word_dict = {}
  duplicate_word_list = []
   
  for word in word_list:
    word = word.lower()
    if word in duplicate_word_dict:
      duplicate_word_dict[word] += 1
    else:
      duplicate_word_dict[word] = 1
  
  for word, count in duplicate_word_dict.items():
    if count > 1:
      duplicate_word_list.append(word)
        
  
  if len(duplicate_word_list) != 0:
    print("Duplicate Words:", end = " ")
    for word in duplicate_word_list:
      print(word, end= " ")
  else:
    print("Duplicate Words:", "None")
  
  
