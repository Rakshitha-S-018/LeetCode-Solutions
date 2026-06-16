class Solution:
    def removeDuplicates(self, n):
        k=0
        for i in n:
            if k==0 or i!=n[k-1]:#if k=0, k-1 becomes -1..we dont need sorting from -1 hence we skip
                n[k]=i
                k+=1
        return k 

        