def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        j = i - 1
        key = arr[i]
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        arr[j + 1] = key

    return arr

arr = [9, 0, 5, 2, 7, 1, 9, 1]
res = insertion_sort(arr)
print(res)
        
            
