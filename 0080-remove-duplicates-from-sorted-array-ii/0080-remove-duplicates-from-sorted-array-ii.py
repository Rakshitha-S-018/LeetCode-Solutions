class Solution:
    def removeDuplicates(self, n):
        if len(n)<=2:
            return len(n)
        else:
            k=2
            
            for i in range(2,len(n)):
                if n[i]!=n[k-2]:
                    n[k]=n[i]
                    k+=1
            return k
        