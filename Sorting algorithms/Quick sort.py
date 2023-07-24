def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    greater = []
    lower = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quicksort(lower) + [pivot] + quicksort(greater)

arr=[6, 3, 8, 2, 9, 2]
print(quicksort(arr))


