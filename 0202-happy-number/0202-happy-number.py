class Solution:
    def isHappy(self, n):
        seen =set() #to check if value in seen
        while n!=1:
            if n in seen:
                return False
            else:
                seen.add(n)
            
            total=0
            
            while n>0:
                digit=n%10
                total=total+ digit*digit
                n=n//10

            n=total
        return True        