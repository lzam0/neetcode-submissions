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
        
        # sort vals dict to obtain the top K values
        topK = sorted(vals.items(), key=lambda item: item[1], reverse=True)[:k]
        print(topK)

        # append it to a new arr to return
        keys = []
        for key, value in topK:
            keys.append(key)

        return keys