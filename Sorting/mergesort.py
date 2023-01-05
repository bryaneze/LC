def mergeSort(arr):
    if len(arr) == 1:
        return arr

    # find middle, split into left and right partitions
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively split
    left = mergeSort(left)
    right = mergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        print(i)
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


nums = [1, 5, 1, 3, 6, 5, 8, 8, 2, 5]
print(mergeSort(nums))
