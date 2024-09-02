def concatenate_array(nums):
  n = len(nums)
  ans = []
  
  for i in range(2*n):
    ans.append(nums[i%n])
  return ans
  

n = int(input())
if n> 0:
  nums = input().split()
  res = concatenate_array(nums)

  for i in res:
    print(i, end=" ")

    