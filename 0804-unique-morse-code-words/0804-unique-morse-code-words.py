class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sett = set()
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i in words:
            letter = ""
            for j in i:
                letter += code[ord(j)-97]
            sett.add(letter)
        return len(sett)