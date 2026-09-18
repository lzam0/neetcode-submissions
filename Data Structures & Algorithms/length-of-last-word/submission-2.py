class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # seperates the word into an arr
        words = s.split()

        # return the last value of arr
        return len(words[-1])