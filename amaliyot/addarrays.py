def merge_two_arrays(arr1, arr2):

    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    result = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < n:
        result.append(arr1[i])
        i += 1

    while j < m:
        result.append(arr2[j])
        j += 1

    return result



arr1 = [1,3,5,7,9,11]
arr2 = [2,4,6,8,12,14]

print(merge_two_arrays(arr1, arr2))