def is_palindrome(text):
    
    new_text = ""
    
    for char in text:
      if char.isalpha():
        new_text += char.lower()
    
    reverse_text = new_text[::-1]
    
    if(new_text == reverse_text):
      print("YES")
    else:
      print("NO")

