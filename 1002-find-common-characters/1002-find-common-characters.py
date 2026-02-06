class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        
        for word in words:
            curr_count = Counter(word)
            for count in counts:
                counts[count] = min(counts[count], curr_count[count])
        
        res = []
        for count in counts:
            for i in range(counts[count]):
                res.append(count)
        
        return res
                