def quicksort(arr, low, high):
    if low < high:
        p = partion(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

def partion(arr, low, high):
    i, j, p = low+1, high, arr[low]
    while True:
        while arr[i] < p and i < j:
            i += 1
        while arr[j] > p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[low], arr[j] = arr[j], arr[low]
            return j 

arr = [1, 5, 3, 7, 8, 6]
k = 4
quicksort(arr, 0, len(arr)-1)
print(arr)
            
