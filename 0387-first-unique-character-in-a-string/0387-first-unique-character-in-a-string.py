class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        
        for c in s:
            if c not in hashmap.keys():
                char_count = s.count(c)
                hashmap[c] = char_count
                
        for key in hashmap.keys():
            if hashmap[key] == 1:
                return s.index(key)
                
        return -1
        
        