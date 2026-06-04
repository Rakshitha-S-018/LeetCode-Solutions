class Solution:
    def countDigits(self, n):
        original = n
        count = 0
        
        while n > 0:
            digit = n % 10
            
            if digit != 0 and original % digit == 0:
                count += 1
            
            n = n // 10
        
        return count