class Solution:
    def numIdenticalPairs(self, n):
        count=0
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i]==n[j]:
                    count=count+1
        return count    

        