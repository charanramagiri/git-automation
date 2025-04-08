from typing import List
__package__ = "solutions"  # Ensure the package is set correctly
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # write your code here
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
        
