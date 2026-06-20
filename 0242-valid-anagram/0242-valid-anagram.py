class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

            
        for ch in t:
            if ch not in freq:
                return False
            else:
                freq[ch]-=1
                if freq[ch]<0:
                    return False
            
        
        for value in freq.values(): #gives freq of each ch
            if value!=0:
                return False
            else:
                return True
                

        