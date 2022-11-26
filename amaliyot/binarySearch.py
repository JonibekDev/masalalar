def binary_search(arr, x):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    mid_value = arr[mid]

    if (mid_value == x):
      return mid
    elif (mid_value < x):
      low = mid + 1
    else:
      high = mid - 1

  return None

arr = [3,4,7,8,10,54,57,79,120,456,458,500,764]
x = 54

print(binary_search(arr, x))