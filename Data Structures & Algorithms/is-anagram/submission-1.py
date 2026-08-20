class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS, countT = {}, {}

        # check if the two strings aren't the same length
        if(len(s) != len(t)):
            return False

        # Iterate through the entire s string and lets check if its inside
        # of the current countS arr
        for i in range(len(s)):
            if s[i] not in countS:
                # Set the initial value to 1
                countS[s[i]] = 1
            else:
                # Incremeent the counter
                countS[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
        
        # check if the two dictionairys are the same
        if(countT == countS):
            return True

        
        return False