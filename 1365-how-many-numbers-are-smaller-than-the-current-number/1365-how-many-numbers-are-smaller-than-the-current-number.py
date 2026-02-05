class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        counts = {}

        for idx, num in enumerate(sorted_num):
            if num not in counts:
                counts[num] = idx
        
        return [counts[num] for num in nums]

        