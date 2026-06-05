class Solution:
    def runningSum(self, n):
        for i in range(1,len(n)):
            n[i]=n[i]+n[i-1]
        return n         