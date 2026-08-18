class Solution:
    def longestConsecutive(self, nums):
        my_set=set()
        for i in range(len(nums)):
            my_set.add(nums[i])
        
        longest=0

        for no in my_set:
            if no-1 not in my_set:
                x=no
                count=1
                while x+1 in my_set:
                    x+=1
                    count+=1
                longest=max(longest,count)
        return longest