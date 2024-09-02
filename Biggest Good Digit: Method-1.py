def biggest_good_digit(num):

  good_digit = -1
  for i in range(len(num)):
    if num[i] == num[i-1] and int(num[i]) > good_digit:
      good_digit = int(num[i])
  return good_digit

