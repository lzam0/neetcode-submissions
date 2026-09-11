class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            char = s[r]
            # check if the curr char is in window
            while char in window:
                # remove the furthest left pointer val
                window.remove(s[l])

                # move the left pointer forward
                l += 1

            # add it to the set
            window.add(char)

            # determine what the max length is 
            maxLength = max(maxLength, r - l + 1)

        return maxLength