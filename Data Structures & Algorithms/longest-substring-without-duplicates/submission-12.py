class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        window = set()

        length = 0

        # iterate through the arr
        for r in range(len(s)):

            # check the character of the right pointer is within the window set
            while s[r] in window:
                # since it is
                # want to remove the value of furthest left within the set
                window.remove(s[l])

                l += 1

            # otherwise add it into the set
            window.add(s[r])

            # check the new max length
            # if length < len(window):
            #     length = len(window)

            length = max(length, len(window))

        return length