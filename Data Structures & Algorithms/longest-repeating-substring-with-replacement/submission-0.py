class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count all of the characters
        count = {}

        # result to return
        result = 0

        l = 0

        for r in range(len(s)):
            # current right pointer size = 1 + 
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # check if the current window is valid

            # window size - the highest value of the count hashmap is GREATER than the amount of k values to be changed
            while (r - l + 1) - max(count.values()) > k:

                #  reduce the current left pointer value by 1
                count[s[l]] -= 1

                # move the left pointer by 1 forward
                l += 1

            # check whether the highest result is still larger than the current window size
            result = max(result, r - l + 1)


        return result
