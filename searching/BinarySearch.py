def binarySearch(arr,n):
    l = 0
    r = len(arr)-1

    while l <=r:
        mid = (l + r) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
        
    return -1


arr = [10, 20, 30, 40, 50]
print(binarySearch(arr, 30))  # Output: 2
print(binarySearch(arr, 60))  # Output: -1


