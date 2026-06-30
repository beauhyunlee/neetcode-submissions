class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for word in nums:
            if word in count:
                return True
            count[word] = 1
        return False

        