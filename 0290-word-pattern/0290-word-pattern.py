class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        map_pw = {}
        map_wp = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in map_pw:
                if map_pw[p] != w:
                    return False
            else:
                map_pw[p] = w

            if w in map_wp:
                if map_wp[w] != p:
                    return False
            else:
                map_wp[w] = p

        return True