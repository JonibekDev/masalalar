def bubble(nums):
  n = len(nums)
  swaps = 0

  for i in range(n-1):
    if nums[i] > nums[i+1]:
      nums[i], nums[i+1] = nums[i+1], nums[i]
      swaps += 1
  return swaps


def bubble_sort(nums):
  n = len(nums)
  for i in range(n-1):
    if bubble(nums) == 0:
      break

nums = [8,2,10,5,1,12,7,9,4]

bubble_sort(nums)
print(bubble(nums))
print(nums)