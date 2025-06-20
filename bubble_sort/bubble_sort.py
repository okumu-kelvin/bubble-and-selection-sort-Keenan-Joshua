def bubble_sort(unsorted_list):
    length = len(unsorted_list)
    sorted_list = []
    while len(sorted_list)!=length:
        i = 0
        while i < (len(unsorted_list) - 1):
            if unsorted_list[i] < unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
            i = i + 1
        sorted_list.append(unsorted_list[i])
        unsorted_list.pop()

    return sorted_list
