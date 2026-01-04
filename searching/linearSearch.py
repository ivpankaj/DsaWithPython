#linear search 


def linearSearch(arr, n):
    for num in arr:
        if num == n:
            return num
    return -1

        
arr = [10, 20, 30, 40]
print(linearSearch(arr, 30))   # Output: 30
print(linearSearch(arr, 50))   # Output: -1

