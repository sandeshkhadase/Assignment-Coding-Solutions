def decode_ciphertext(ciphertext, key):
  
  decoded_text = ""
  for ch in ciphertext:
    
    if ch.isalpha():
      idx = key.index(ch)
      decoded_text += chr(65 + idx)
      
    else:
      decoded_text += ch
      
  print(decoded_text)

