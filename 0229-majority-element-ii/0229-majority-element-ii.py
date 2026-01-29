class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        result = []
        for num in counts:
            if counts[num] > n // 3:
                result.append(num)
        
        return result