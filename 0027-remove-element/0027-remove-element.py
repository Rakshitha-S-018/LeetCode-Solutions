class Solution:
    def removeElement(self, n,val):
        k=0
        for i in n:
            if i !=val:
                n[k]=i #if value!=k add that to k[0]
                k+=1
        return k