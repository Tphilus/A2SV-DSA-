class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        counts = {}

        for i, num in enumerate(sorted_num):
            if num not in counts:
                counts[num] = i
                
        return [counts[num] for num in nums]