class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this is how im thinking about this first
        # its quite similar to the problem we just worked on 'valid anagram'

        # however we should sort the chars of each word
        # example: cat -> act
        
        group = {}
        for i in range(len(strs)):
            currWord = strs[i]

            sortedStr = tuple(sorted(currWord))
                    
            if sortedStr not in group:
                # lets add it to the group
                group[sortedStr] = [currWord]
            else:
                # otherwise add the currWord
                group[sortedStr].append(currWord)
                
        return list(group.values())