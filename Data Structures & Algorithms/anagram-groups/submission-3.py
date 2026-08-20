class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for i in range(len(strs)):
            currStr = strs[i]
            # lets reorganise the current string
            
            sortedStr = tuple(sorted(currStr))
            # print(sortedStr)

            if sortedStr not in groups:
                print("New Grouping:", currStr)
                groups[sortedStr] = [currStr]
            else:
                print("Added to existing Grouping:", currStr)
                groups[sortedStr].append(currStr)


        print(groups)
        return list(groups.values())