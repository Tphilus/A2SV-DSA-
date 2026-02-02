class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_dic = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }

        res = 0
        for sign in operations:
            res += operations_dic.get(sign, 0)
        
        return res