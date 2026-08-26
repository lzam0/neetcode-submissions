class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first thing to check if s and t strings length are the same
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}

        for i in range(len(s)):
            char = s[i]

            if char not in dictS:
                dictS[char] = 1
            else:
                dictS[char] += 1

        for i in range(len(t)):
            char = t[i]

            if char not in dictT:
                dictT[char] = 1
            else:
                dictT[char] += 1

        if dictS != dictT:
            return False
            
        return True