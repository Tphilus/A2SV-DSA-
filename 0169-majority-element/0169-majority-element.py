class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1

            if counts[i] > n // 2:
                return i