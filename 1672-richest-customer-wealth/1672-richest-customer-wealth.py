class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        cols = len(accounts[0])

        mx = 0
        for row in range(rows):
            counts = 0
            for col in range(cols):
                counts += accounts[row][col]
            mx = max(mx, counts)
        
        return mx
            
                
            