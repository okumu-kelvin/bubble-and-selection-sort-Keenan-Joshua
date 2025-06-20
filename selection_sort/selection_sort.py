def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr