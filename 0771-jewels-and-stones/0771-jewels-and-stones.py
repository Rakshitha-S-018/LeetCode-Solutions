class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        count=0
        for i in stones:
            if i in jewels:
                count=count+1
        return(count)      