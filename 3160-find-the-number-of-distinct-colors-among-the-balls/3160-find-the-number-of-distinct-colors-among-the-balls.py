class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_counts = {}
        result = []
        
        for ball, color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            
            ball_color[ball] = color
            
            color_counts[color] = color_counts.get(color, 0) + 1
            
            result.append(len(color_counts))
            
        return result