class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        flag = 0
        if len(s) < 3:
            pass
        elif len(s) >= 3 :
            
            for i in range(0 , len(s) - 2):
                substring = s[i : i + 3]
                flag = 0
                for c in substring:
                    if substring.count(c) == 1:
                        flag = flag + 1
                    if flag == 3:
                        count = count + 1
                        
        return count 
        
        