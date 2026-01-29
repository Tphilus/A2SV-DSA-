class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        majority = 0
        res = 0

        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)

            if hashMap[i] > majority:
                res = i
                majority = hashMap[i]
        
        return res