class Solution:
    def longestCommonPrefix(self, s):
        if len(s)==0:
            return""
        prefix=s[0]
        for ch in s:
            while not ch.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix        


        