class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = [ ]
        for i in range(0 , len(nums) - 1 ):
            for j in range(i+1 , len(nums)):
                if(nums[i] + nums[j] == target):
                    return_list.append(i)
                    return_list.append(j)

        return return_list