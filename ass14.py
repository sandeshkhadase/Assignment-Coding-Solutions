def calculate_median(scores):
  scores.sort()
  
  length = len(scores)
  
  if length % 2 == 0:
    n1 = scores[length // 2 - 1]
    n2 = scores[length // 2]
    n = (n1 + n2) / 2
    print(n)
  
  else:
    n = scores[length // 2]
    print(n)
