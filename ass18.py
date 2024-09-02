def vigenere_encrypt(plaintext, key):
  text_len = len(plaintext)
  key_len = len(key)
      
  words_list = plaintext.split()
  new_words_list = []
 
  i = 0
  for word in words_list:
    new_word = ""
    for j in range(len(word)):
      new_word +=  chr(((ord(word[j]) + ord(key[i % key_len])) % 26) + 65)
      i += 1  
    new_words_list.append(new_word)
    
  cypher_text = " ".join(new_words_list)
      
  return cypher_text
