class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        k = -1
        
        for i in range(0 , len(haystack)):
            
            if(haystack[i:len(needle) + i] == needle and (len(needle) + i) <= len(haystack) ):
                k = i
                break
        
        return k
            
        