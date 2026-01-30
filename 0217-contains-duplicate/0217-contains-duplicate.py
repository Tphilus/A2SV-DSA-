class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_num = len(nums)
        unique_len = len(set(nums))

        return not len_num == unique_len