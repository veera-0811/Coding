# Link :- https://neetcode.io/problems/anagram-groups/question?list=neetcode150

# Naive Solution :- O(n*klogk) where n is the number of words and k is the length of the longest word
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        if n == 1:
            return [strs]

        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)
        return list(d.values())

# Optimal Solution :- O(n*k) where n is the number of words and k is the length of the longest word
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        if n == 1:
            return [strs]

        d = {}
        for word in strs:
            freq = [0]*26
            for ch in word:
                ind = ord(ch) - 97
                freq[ind] += 1

            key = tuple(freq)
            if key not in d:
                d[key] = []
            d[key].append(word)
        return list(d.values())