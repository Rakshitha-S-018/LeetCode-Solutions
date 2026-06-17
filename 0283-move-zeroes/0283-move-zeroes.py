class Solution:
    def moveZeroes(self, n):
       k=0
       for i in range(len(n)):
        if n[i]!=0:
            n[k]=n[i]
            k+=1
       while k<len(n):
        n[k]=0
        k+=1 