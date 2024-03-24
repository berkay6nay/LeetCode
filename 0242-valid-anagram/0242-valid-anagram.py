class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        
        for c in s:
            if c not in hashmap_s.keys():
                hashmap_s[c] = s.count(c)
                
        for c in t:
            if c in hashmap_s.keys():
                hashmap_s[c] = hashmap_s[c] - 1  
            else:
                return False
            
        for key in hashmap_s.keys():
            if hashmap_s[key] != 0:
                return False
            
        return True
        