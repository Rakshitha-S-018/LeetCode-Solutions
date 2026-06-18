class Solution:
    def productExceptSelf(self, nums):
        ls=[1]*len(nums)
        rs=[1]*len(nums)
        fs=[1]*len(nums)  

        for i in range(1,len(nums)): # as we e doing ls[i] with ls[i-1 ] we r starting range from 1
            ls[i]=ls[i-1] * nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            rs[j]=rs[j+1] * nums[j+1]

        for k in range(len(nums)):
            fs[k] = ls[k] * rs[k]

        return fs


