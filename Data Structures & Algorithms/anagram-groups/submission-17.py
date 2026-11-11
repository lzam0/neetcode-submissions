class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # get the individal words
        # reorder the words by using sort() func
        # then append it to the groups hashmap afterwards
        for word in strs:
            anagram = tuple(sorted(word))

            if anagram not in groups:
                groups[anagram] = []

            groups[anagram].append(word)

        return list(groups.values())