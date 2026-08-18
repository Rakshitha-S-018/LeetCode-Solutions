class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i=0
        j=len(n)-1
        while j>i:
            if n[i]+n[j]<target:
                i+=1
            elif n[i]+n[j]>target:
                j-=1
            else:
                return (i+1,j+1)
                
        