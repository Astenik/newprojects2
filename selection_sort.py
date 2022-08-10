def selection_sort(nums):
      '''this function sorts numbers' list whit selection-sort algorithm.'''
      for ind1 in range(len(nums)):
            min_num_index = ind1 
            for ind2 in range(ind1 + 1, len(nums)):
                  if nums[ind2] < nums[min_num_index]:
                       nums[ind2], nums[min_num_index] = nums[min_num_index], nums[ind2]
      return nums 
nums = [48, 940, 8934, 0, 8]
print(f"your sorted list whit selection sort algorithm is: {selection_sort(nums)}")
