
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        """
        Function to find how many numbers are smaller than each element in the array.
        Uses a brute force approach for comparison.
        """
        n = len(nums)
        result = [0] * n
        
        # Brute force comparison
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1
            result[i] = count
        
        return result
