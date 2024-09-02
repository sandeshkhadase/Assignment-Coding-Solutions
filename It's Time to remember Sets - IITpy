def factors(n):
  factors = set()
  for i in range(1, n+1):
    if n % i == 0:
      factors.add(i)
  return factors

def common_factors(a, b):
  factors_of_a = factors(a)
  factors_of_b = factors(b)
  common_factors = factors_of_a & factors_of_b
  return common_factors

def factors_upto(n):
  factors_dict = {}
  for i in range(1, n + 1):
    factors_dict[i] = factors(i)
    
  return factors_dict
    
