class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # seperates the word into an arr
        word = s.split()

        lengthWord = len(word) -1

        print(lengthWord)

        ans = len(word[lengthWord])


        return ans