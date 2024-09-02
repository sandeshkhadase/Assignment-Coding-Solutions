import math
def biggest_good_digit(num):

  good_digit = -1
  last_digit = None
  
  for digit in num:
    digit = int(digit)
    if digit == last_digit and last_digit > good_digit:
      good_digit = digit

    last_digit = digit
    
  return good_digit

