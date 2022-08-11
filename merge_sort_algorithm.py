def merge_sort(nums):
     '''this function sorts the nums list using merge sort algorithm.'''
     if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(right)
        merge_sort(left)
        i = j = k = 0
        while i < len(left) and j < len(right):
              if left[i] < right[j]:
                 nums[k] = left[i]
                 i += 1
              else:
                  nums[k] = right[j]
                  j += 1 
              k += 1
        # checking if any element was left
        while i < len(left):
              nums[k] = left[i]
              i += 1
              k += 1
        while j < len(right):
               nums[k] = right[j]
               j += 1
               k += 1
     return nums
nums = [23, 859, 8, 0, 74]
print(f"your sorted list is: {merge_sort(nums)}")
