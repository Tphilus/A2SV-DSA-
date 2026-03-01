class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        w = nums[0]
        x = nums[1]
        y = nums[-1]
        z = nums[-2]

        output = abs((w * x) - (y * z))
        return output