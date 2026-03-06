class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total = 0

        for row in nums:
            row.sort()
        
        for i in range(len(nums[0])):
            mx = 0
            for j in range(len(nums)):
                mx = max(nums[j][i], mx)
            
            total += mx
        
        return total
