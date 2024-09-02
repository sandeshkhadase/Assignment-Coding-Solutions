import string

def get_most_frequent_word(lines):
    words_list = []
    
    for line in lines:
      line = line.translate(str.maketrans('', '', string.punctuation))
      for word in line.split():
        words_list.append(word.lower())
        
    freq_dict = {}
    for word in words_list:
      if word in freq_dict:
        freq_dict[word] += 1
      else:
        freq_dict[word] = 1
    
    most_freq_word = ""
    max_count = 0
    for word, count in freq_dict.items():
      if count > max_count:
        max_count = count
        most_freq_word = word
        
    if len(words_list):
      return most_freq_word
    
    else:
      return "No valid words found in the list."
