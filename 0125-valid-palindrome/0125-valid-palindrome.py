class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        for ch in s:
            if not ch.isalnum():
                s=s.replace(ch,"")
        if s==s[::-1]:
            return True
        else:
            return False
        