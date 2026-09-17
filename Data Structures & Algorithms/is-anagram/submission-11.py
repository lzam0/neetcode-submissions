class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {},{}

        # if lenghts are the same for strings
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1

        for i in range(len(t)):
            if t[i] in dictT:
                dictT[t[i]] += 1
            else:
                dictT[t[i]] = 1

        
        return dictS == dictT
