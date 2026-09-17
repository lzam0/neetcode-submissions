class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {},{}

        # if lenghts are the same for strings
        if len(s) != len(t):
            return False


        # loop through arr
        for i in range(len(s)):
            # check if the dict has this char
            # if it doesn't return 0 otherwise return the value
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

            
        
        return dictS == dictT
