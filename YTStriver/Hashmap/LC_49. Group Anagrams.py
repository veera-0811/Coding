class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        if n == 1:
            return [strs]
        h = {}
        for word in strs:
            w = "".join(sorted(word))
            if w in h:
                h[w].append(word)
            else:
                h[w] = [word]
        return list(h.values())

# Sample Input
strs = ["eat","tea","tan","ate","nat","bat"]            #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(strs))