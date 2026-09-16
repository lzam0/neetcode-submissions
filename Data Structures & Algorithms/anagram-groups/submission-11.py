class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
            # sort the current word
            word = strs[i]
            stringSort = tuple(sorted(word))

            # if the current word in the group
            if stringSort  in groups:
                # if it is then add it along with the other word
                groups[stringSort].append(word)
            else: # otherwise the word is not the grouping
                # cretea a new instance of the word grouping in the dict
                groups[stringSort] = [word]


        return list(groups.values())