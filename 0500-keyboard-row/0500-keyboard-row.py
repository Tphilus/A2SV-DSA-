class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        res = []
        for word in words:
            uniq_word = set(word.lower())
            if uniq_word <= first_row or uniq_word <= second_row or uniq_word <= third_row:
                res.append(word)
        
        return res

        
            