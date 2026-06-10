class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return[]
        else:
            phone={
                "2" : "abc",
                "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
            result=[]
            def backtrack(index,path): #path=output we r building
                if index==len(digits):
                    result.append(path)
                    return

                for ch in phone[digits[index]]: #digits[0] = "2" , phone["2"] = "abc"
                    backtrack(index+1,path+ch)
            backtrack(0,"")
            return result
