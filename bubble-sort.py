def bubble_sort(nums):
       '''this function sorts the list using bubble-sort algorithm.'''
       for i in range(len(nums)):
           count = 0
           for j in range(len(nums) - 1 - i):
               if nums[j] > nums[j + 1]:
                      nums[j], nums[j + 1] = nums[j + 1], nums[j]
                      count += 1 
           if count == 0:
               break
       return nums 
lst = [2, 84, 859, 0, 90, 4]
print(f"your sorted list is: {bubble_sort(lst)}")
