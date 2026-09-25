class Solution:
    # Approach: Hashing using two dictionaries                    Time Complexity: O(n)  Space Complexity: O(n)
    # Key Idea: We can use two dictionaries to map characters in the pattern to words in the string and vice versa. If at any point the mapping is inconsistent, we return False. If we successfully map all characters to words and vice versa, we return True.
    def wordPattern(self, pattern,s):
        n = len(pattern)
        words = s.split()
        if n != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for i in range(n):
            c = pattern[i]
            w = words[i]
            if c in char_to_word and char_to_word[c]!=w:
                return False
            if w in word_to_char and word_to_char[w]!=c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True


    # Approach: dictionary + set to check for bijection                    Time Complexity: O(n)  Space Complexity: O(n)
    # Key Idea: We can use a dictionary to map characters in the pattern to words in the string and a set to keep track of the words that have already been mapped. If at any point the mapping is inconsistent or a word has already been mapped to a different character, we return False. If we successfully map all characters to words and vice versa, we return True.
    def wordPattern1(self, pattern, s):
        n = len(pattern)
        words = s.split()
        if n != len(words):
            return False
        char_to_word = {}
        visited = set()
        for i in range(n):
            c = pattern[i]
            w = words[i]
            if c in char_to_word:
                if char_to_word[c]!=w:
                    return False
            else:
                if w in visited:
                    return False
                char_to_word[c] = w
                visited.add(w)
        return True


# Example usage
pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))  # Output: True

# Example usage
pattern = "abba"
s = "dog cat cat fish"
print(Solution().wordPattern1(pattern, s))  # Output: False