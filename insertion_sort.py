def insertion_sort(nums):
       '''this function sorts numbers' list whit insertion-sort algorithm.'''
       for ind1 in range(1, len(nums)):
           ind2 = ind1 - 1
           key = nums[ind1]
           while ind2 >= 0 and key < nums[ind2]:
                nums[ind2 + 1] = nums[ind2]
                ind2 -= 1
           nums[ind2 + 1] = key
       return nums 
nums = [85, 0, 74, 8, 72]
print(f"your sorted list, sorted with insertion sort is: {insertion_sort(nums)}")
