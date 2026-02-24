class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(names)):
            mx = i
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[mx]:
                    heights[j], heights[mx] = heights[mx], heights[j]
                    names[j], names[mx] = names[mx], names[j]
        
        return names