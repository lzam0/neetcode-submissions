class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # lets sort the words

        for i in range(len(strs)):

            sortedString = tuple(sorted(strs[i]))

            if sortedString in groups:
                # we add the original word into the grouping
                groups[sortedString].append(strs[i])
            else:
                # make a new grouping
                groups[sortedString] = [strs[i]]
        return list(groups.values())