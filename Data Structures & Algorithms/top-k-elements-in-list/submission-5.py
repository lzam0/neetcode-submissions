class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}

        for i in range(len(nums)):
            currNum = nums[i]

            if(currNum not in vals):
                vals[currNum] = 1
            else:
                vals[currNum] += 1
        
        sortedVals = sorted(vals.items(), key=lambda item: item[1], reverse=True)[:k]

        keys = []
        for key, value in sortedVals:
            keys.append(key)

        return keys