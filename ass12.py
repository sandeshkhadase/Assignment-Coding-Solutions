def solve(N, arr):
    
    new_arr = list(set(arr))
    new_arr.sort()
    
    if len(new_arr) >= 3:
      for x in new_arr[0:3]:
        print(x, end=" ")
      print()    
      for x in new_arr[-3:]:
        print(x, end=" ")
      
    else:
      print("Not Possible")
      print("Not Possible")