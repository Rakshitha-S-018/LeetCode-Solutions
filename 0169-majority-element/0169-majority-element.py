class Solution:
    def majorityElement(self, n):
        count=0
        candidate=None
        for i in n:
            if count==0:
                candidate=i
            if i==candidate:
                count=count+1
            else:
                count-=1
        return candidate 