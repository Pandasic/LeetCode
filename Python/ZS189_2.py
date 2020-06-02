class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words[0] = words[0].lower()
        words = list(enumerate(words))
        wordSize =len(words)
        #words.sort(key = lambda pair: -1*len(pair[1])*len(words) + pair[0])
        words.sort(key = lambda pair:len(pair[1])*wordSize + pair[0])
        res = ""
        for w in words:
            res += w[1] + " "
        res = res[0].upper() + res[1:-1]
        return res

s = Solution()
print(s.arrangeWords("Leetcode is cool"))
print(s.arrangeWords("Keep calm and code on"))