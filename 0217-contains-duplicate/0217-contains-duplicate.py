class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_num = len(nums)
        unique_len = len(set(nums))

        if len_num != unique_len:
            return True
        else:
            return False