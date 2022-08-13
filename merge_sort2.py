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
        while i < len(left):
              nums[k] = left[i]
              i += 1
              k += 1
        while j < len(right):
               nums[k] = right[j]
               j += 1
               k += 1
     return nums
nums1 = [1, 6, 4, 8, 89, 0, 0, 0, 0, 0, 0, 0]
nums2 = [67, 8, 3, 90, 786, 1, 0]
m = len(nums2) - 1
n = len(nums1) - m 
j = 0
for i in range(n, n + m):
     nums1[i] = nums2[j]
     j += 1
print(f' your sorted list consists of nums1 and nums2 lists is: {merge_sort(nums1)}')
