class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        flag = len(nums)/2
        
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = nums.count(num)
        for key in hashmap.keys():
            if hashmap[key] > flag:
                return key
        
        