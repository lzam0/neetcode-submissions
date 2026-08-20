class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # Iterate through string s
        for i in range(len(s)):
            # Get the value of the curr index of the string
            countS[s[i]] = 1 + countS.get(s[i], 0)

            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True