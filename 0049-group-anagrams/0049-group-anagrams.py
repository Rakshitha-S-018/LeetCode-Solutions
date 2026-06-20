class Solution:
    def groupAnagrams(self, strs):
        hashmap={}
        
        for word in strs:
            key="".join(sorted(word))

            if key not in hashmap:
                hashmap[key]=[] #create empty list for that key
            hashmap[key].append(word)

        return list(hashmap.values()) # returns in form of list