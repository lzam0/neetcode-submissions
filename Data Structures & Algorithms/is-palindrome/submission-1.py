class Solution:
    def isPalindrome(self, s: str) -> bool:
        # essentially can implement the two pointer solution

        # string = "WORD"
        # P1 = W and P2 = D
        # then we can move the pointers inward and then check if the two pointer values are the same
        
        # assign the left and right pointer
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                # increment left pointer pos by 1
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            # move pointer 
            left, right = left + 1, right - 1
        return True
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))