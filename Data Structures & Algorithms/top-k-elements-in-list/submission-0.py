class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # holds counts of each number
        count = {}
        # create the buckets
        freq = [[] for _ in range(len(nums) + 1)]

        # go through every value in nums and count
        for n in nums:
            count[n] = 1 + count.get(n, 0) # returns 0 if not found 
        
        # append number into buckets according to count
        for n, c in count.items():
                freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # descending order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res