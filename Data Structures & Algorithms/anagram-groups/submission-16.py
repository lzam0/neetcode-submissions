class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # lets sort the words

        for word in strs:

            sortedString = tuple(sorted(word))

            if sortedString in groups:
                # we add the original word into the grouping
                groups[sortedString].append(word)
            else:
                # make a new grouping
                groups[sortedString] = [word]
        return list(groups.values())