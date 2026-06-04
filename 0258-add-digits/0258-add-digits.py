class Solution:
    def addDigits(self, n):
        while n>=10:
            count=0
            while n>0:
                digit=n%10
                count=count+digit
                n=n//10
            n=count
        return n   
