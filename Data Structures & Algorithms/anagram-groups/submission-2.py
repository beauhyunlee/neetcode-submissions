class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for word in strs:
            count = [0] * 26# initialize the array
            for char in word:
            # ascii chart to put into hashmap
                count[ord(char)-ord("a")] += 1
                # this is going to be the key and the values are going to be the words
            res[tuple(count)].append(word)
        return list(res.values())