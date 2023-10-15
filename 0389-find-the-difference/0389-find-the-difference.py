class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        asci_s = 0
        asci_t = 0
        
        for c in s:
            asci_s = ord(c) + asci_s
            
        for c in t:
            asci_t = ord(c) + asci_t
            
        return chr(asci_t - asci_s)
            
        