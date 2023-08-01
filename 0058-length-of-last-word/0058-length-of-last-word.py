class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #word = ""
        length = 0
        
        for char in s[::-1]:
            
            if(char != " "):
                length += 1
            
            if(char == " " and length > 0):
                break
            
            
            
        return length
            
        """
        for char in word:
            
            if(char != " "):
                length += 1
        
        return length """
            
            
            
            
            
            
        