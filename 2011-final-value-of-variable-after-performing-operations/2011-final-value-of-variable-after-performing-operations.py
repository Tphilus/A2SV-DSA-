class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operation_dic = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }

        counts = 0
        for sign in operations:
            counts += operation_dic.get(sign, 0)
        
        return counts
            
            