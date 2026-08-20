class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''

        for char in s:
            # check if the char is an alphanumeric 
            if char.isalnum():
                string += char.lower()

        return string == string[::-1]