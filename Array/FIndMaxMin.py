# find the max and min from an array

def findMax(arr):
    maxNum = arr[0]

    for num in arr:
        if num > maxNum:
            maxNum = num


    return maxNum

arr = [3, 7, 2, 9, 5]
print(findMax(arr))


def findMin(arr):
    minNum = arr[0]

    for num in arr:
        if num < minNum:
            minNum = num
        
    return minNum


arr = [3, 7, 2, 9, 5]
print(findMin(arr))

