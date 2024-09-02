def sort_books_ascending(books_list):
  
  n = len(books_list)
  
  for i in range(n-1):
    
    isSorted = True
    
    for j in range(n-1-i):
      if books_list[j][1] > books_list[j+1][1]:
        books_list[j], books_list[j+1] = books_list[j+1], books_list[j]
        isSorted = False
        
    if isSorted:
      break
    
  return books_list
  
def sort_books_descending(books_list):
  n = len(books_list)
  
  for i in range(n-1):
    
    isSorted = True
    
    for j in range(n-1-i):
      if books_list[j][1] < books_list[j+1][1]:
        books_list[j], books_list[j+1] = books_list[j+1], books_list[j]
        isSorted = False
        
    if isSorted:
      break
    
  return books_list


