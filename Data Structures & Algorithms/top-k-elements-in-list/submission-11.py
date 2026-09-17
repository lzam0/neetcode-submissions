class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            # if number in the count dict
            if n in count:
                # if it is then increase counter
                count[n] += 1
            else:
                # if not then add it
                count[n] = 1

        # return the largest K elements within a dict
        # use a nlargest with heapq, based on the value and return the key
        topK = heapq.nlargest(k, count, key=count.get)
        
        return topK