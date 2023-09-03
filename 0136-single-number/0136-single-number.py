class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        new_list = []
        
        for number in nums:
            
            if number not in new_list:
                new_list.append(number)
                
            elif number in new_list:
                new_list.remove(number)
                
        result = new_list[0]
        return result
        
        