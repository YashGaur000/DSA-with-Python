def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root (i) with the largest element found
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the max-heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)






