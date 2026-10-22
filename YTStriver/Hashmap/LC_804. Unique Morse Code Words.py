class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        d = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        s = set()
        for word in words:
            temp = ""
            for ch in word:
                temp += d[ch]
            s.add(temp)
        return len(s)

words = ["gin","zen","gig","msg"]           # Output: 2
print(Solution().uniqueMorseRepresentations(words))
'''Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".'''