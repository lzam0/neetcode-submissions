class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT, countS = {}, {}

        for char in s:
            if char not in countS:
                # create a new counter char
                countS[char] = 1
            else:
                # increment the counter
                countS[char] += 1

        
        for char in t:
            if char not in countT:
                # create a new counter char
                countT[char] = 1
            else:
                # increment the counter
                countT[char] += 1

        if countS != countT:
            return False
            
        return True