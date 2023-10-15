class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        occ = 0
        
        for c in s:
            if c == letter:
                occ = occ + 1
                
        return int((occ/len(s))*100)
            
        