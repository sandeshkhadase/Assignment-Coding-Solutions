def string_score(s):
  sum = 0
  prev_char = ""
  
  for char in s:
    if prev_char != "":
      sum += abs(ord(char) - ord(prev_char))
      prev_char = char
    else:
      prev_char = char
  
  return sum 

