class Solution:
    def isIsomorphic(self, s, t):
        map_st={}
        map_ts={}
        for i in range (len(s)):
            ch_s = s[i]
            ch_t = t[i]

            if ch_s in map_st: # if ch is already there in seen
                if map_st[ch_s]!=ch_t:
                    return False
            else:
                map_st[ch_s]=ch_t #e:a
                
            if ch_t in map_ts:
                if map_ts[ch_t]!=ch_s:
                    return False
            else:
                map_ts[ch_t]=ch_s
        
        return True


        