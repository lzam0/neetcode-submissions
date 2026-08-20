class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            currVal = nums[i]

            # if the current value isnt inside of the dict
            if currVal not in vals:
                vals[currVal] = 1
            else:
                # incremenet counter
                vals[currVal] += 1

        print(vals)

        topK = sorted(vals.items(), key=lambda item: item[1], reverse=True)[:k]

        keys = []
        for key, value in topK:
            keys.append(key)
        return keys