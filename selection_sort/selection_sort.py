def selection_sort(arr):
    length = len(arr)
    sorted_arr=[]
    while len(sorted_arr)!=length:
        i = 0
        min_value = arr[i]
        x = i
        while x < len(arr):
            if min_value > arr[x]:
                i = x
                min_value = arr[i]
            x = x + 1
        arr[0], arr[i] = arr[i], arr[0]
        sorted_arr.append(min_value)
        arr.pop(0)
    return sorted_arr
