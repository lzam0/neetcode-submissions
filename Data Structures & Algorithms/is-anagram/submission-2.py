class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  check if the two strings are the same lenght
        if(len(s) != len(t)):
            return False

        # char: count
        dictS, dictT = {},{}

        # appending chars into two seperate dicts
        for i in range(len(s)):
            print(s[i])
            if s[i] not in dictS:
                dictS[s[i]] = 1
            else:
                dictS[s[i]] += 1
        
        for i in range(len(t)):
            print(t[i])
            if t[i] not in dictT:
                dictT[t[i]] = 1
            else:
                dictT[t[i]] += 1

        print(dictS, dictT)
        # check if the dictionaries are the same
        if dictS == dictT:
            return True
        return False
