from typing import List
__package__ = "solutions"  # Ensure the package is set correctly
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #write your code here
        result = []
        
        for i in range(len(nums)):  # Iterate through each element
            count = 0
            for j in range(len(nums)):  # Compare with every other elementjhjvuhibib
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        
        return result
