class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')]+=1
            sublists[tuple(count)].append(word)
        return list(sublists.values())