def reverse(arr):
    left, right = 0, 4
    while(left < right):
        swap(arr,left,right)
        left += 1
        right -= 1
    return arr

def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

arr = [1,2,3,4,5]
print(reverse(arr))