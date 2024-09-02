def solve(N):
  if N >= 0:
    fact = 1
    for i in range(1, N+1):
      fact *= i
    print(fact)
    
  else:
    print("Factorial Not Available")
