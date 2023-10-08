def maxprofit(arr):
    l, r = 0, 1
    maxp = 0
    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            maxp = max(maxp, profit)
        else:
            l += 1
        r += 1
    print(maxp)


array = [10, 1, 2, 3, 7, 4, 5, 1, 6, 9]
maxprofit(array)


