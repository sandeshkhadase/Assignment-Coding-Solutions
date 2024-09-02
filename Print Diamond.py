def print_diamond(n):
  for i in range(2*n):
    if i < 2 * n // 2:
      for j in range(n-i-1):
        print(" ", end= "")
      for k in range(2*i+1):
        print("*", end="")
      print()
    
    else:
      for j in range(i-n+1):
        print(" ", end= "")
      for k in range(2*n - (2*(j+1) + 1) ):
        print("*", end="")
      print()


