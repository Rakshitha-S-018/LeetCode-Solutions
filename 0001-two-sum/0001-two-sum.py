class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            diff= target-nums[i]
            
            if diff in seen:
                return [seen[diff],i] #returns index of diff and current index val
            else:
                seen[nums[i]] =i # add num to seen with its index


        