def is_leap_year(date_string):
  year = int(date_string[0:4])
  
  if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False
