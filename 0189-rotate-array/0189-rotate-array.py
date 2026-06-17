class Solution:
    def rotate(self, nums, k):
        n=len(nums)
        rotations=k%n
        for _ in range(0,rotations):
            e=nums.pop()
            nums.insert(0,e) #insert e at 0

       