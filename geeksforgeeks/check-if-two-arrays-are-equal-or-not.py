class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        
        a.sort()
        b.sort()
        
        if len(a) != len(b):
            return False
        
        return a == b