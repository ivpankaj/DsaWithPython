#first non repeating element from an array

def findfirstnonrepeatingelement(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == 1:
            return num

    return None
