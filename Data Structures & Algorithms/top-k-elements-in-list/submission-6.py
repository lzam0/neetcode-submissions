class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lets put the nums arr into a dict first
        # value: counter
        counter = {}

        for i in range(len(nums)):
            currNum = nums[i]

            if currNum not in counter:
                # set initial counter value
                counter[currNum] = 1
            else:
                # increment counter
                counter[currNum] += 1

        
        sort = sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]

        keys = []
        for key, value in sort:
            keys.append(key)

        print(sort)

        return keys