def bubble_sort(arr):

    n = len(arr)
    
    for i in range(n-1):
        isSorted = True
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False

        if isSorted:
            break

arr = [1, 2, 3, 4, 6, 5]
bubble_sort(arr)
print("Sorted Array:", arr)
