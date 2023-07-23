class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = 0
        for i in range(0 , len(nums)):
            if(i == 0 and target < nums[i]):
                return 0
            if(nums[i] == target):
                output = i
                return output
            
            if(i == len(nums) - 1):
                return (i + 1)
            if(target > nums[i] and target < nums[i+1]):
                return (i + 1) 
        
        