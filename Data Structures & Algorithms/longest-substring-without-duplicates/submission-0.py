class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        max_len = 0

        for right in range(len(s)):

            # essentially check if the right current right value is in the window set
            while s[right] in window:

                # we 'shrink' the window from the left until the duplicate is removed 
                window.remove(s[left])

                # increment the left pointer
                left += 1

            # expands the window through the right pointer
            window.add(s[right])

            # keep track of the largest window seen so far 
            # r - l + 1 is the curr window size then compare to the previous best
            max_len = max(max_len, right - left + 1)
            
        return max_len
