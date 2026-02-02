class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        my_set = set(friends)
        result = []
        
        for num in order:
            if num in my_set:
                result.append(num)
        
        return result