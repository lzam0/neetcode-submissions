class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(strs)

        words = {}
        
        for i in range(len(strs)):
            # print(strs[i])
            sortedStr = tuple(sorted(strs[i]))
            print(sortedStr)
            if sortedStr not in words:
                print(strs[i],sortedStr, " in arr already")
                words[sortedStr] = [strs[i]]
            else: 
                print(strs[i],sortedStr, "not in arr already")
                words[sortedStr].append(strs[i])

                
        print(words)
        return list(words.values())