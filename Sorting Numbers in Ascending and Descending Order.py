def sort_ascending(arr):
  n = len(arr)

  for i in range(n-1):
    isSorted = True
    for j in range(n-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        isSorted = False

    if isSorted:
      break
    
  return arr

def sort_descending(arr):
  n = len(arr)

  for i in range(n-1):
    isSorted = True
    for j in range(n-1-i):
      if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        isSorted = False

    if isSorted:
      break
    
  return arr


