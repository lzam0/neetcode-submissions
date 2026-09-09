class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}
        
        # we check if the length of s and t are the same: then we can continue

        # iterate through the length of s
            # check if curr char is in the dict then add it if not otherwise increment the value
            #
            
        # iterate through the length of the
            # append char into the dict

        # check if dictS == dictT
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

        if dictS == dictT:
            return True
        
        return False

        