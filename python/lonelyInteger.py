def lonely_integer(arr):
    if len(arr) > 2:
        lonely_number = arr[0]
        for number in arr[1:]:
            lonely_number = lonely_number ^ number
        
        return lonely_number
    else:
        return "Error: Array must contain min 3 numbers"

print(lonely_integer([1,1,2,3,5,3,4,6,6,5,4]))