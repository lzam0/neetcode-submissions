class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # annagram
        # contain same characters
        # each char appearing the same number of times
        # REGARDLESS of order

        countT, countS = {}, {}

        # check if the lengths of strings are the same
        # return false


        # then we can add each char into hashmap
        # -> add it into hashmap
        # -> eg: r: 2
        # then check if hashmaps are the same
        


        # --- code
        if len(s) != len(t):
            return False

        for char in s:
            if char not in countS:
                # append it into hashmap
                countS[char] = 1
            else:
                # already in hashmap
                countS[char] += 1
        
        for char in t:
            if char not in countT:
                countT[char] = 1
            else:
                countT[char] += 1
            
        return countT == countS 