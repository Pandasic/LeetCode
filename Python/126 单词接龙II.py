"""
126. 单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
通过次数8,551提交次数27,138
"""

#BFS + DFS
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_bag = set(wordList)
        if endWord not in word_bag:
            return []
        
        word_bag.add(beginWord)
        
        distance = self.bfs(endWord, word_bag)
        
        results = []
        self.dfs(beginWord, endWord, word_bag, distance, [beginWord], results)
        
        return results
    
    def bfs(self, begin_word, word_bag):
        queue = [begin_word]
        distance = {}
        distance[begin_word] = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_word = queue.pop(0)
                for next_word in self.get_next_words(curr_word, word_bag):
                    if next_word not in distance:
                        distance[next_word] = distance[curr_word] + 1
                        queue.append(next_word)
        return distance
    
    def dfs(self, curr_word, target, word_bag, distance, path, results):
        if curr_word == target:
            results.append(list(path))
            return
        for next_word in self.get_next_words(curr_word, word_bag):
            if distance[next_word] != distance[curr_word] - 1:
                continue
            path.append(next_word)
            self.dfs(next_word, target, word_bag, distance, path, results)
            path.pop()
    
    def get_next_words(self, curr_word, word_bag):
        next_words = []
        for i in range(len(curr_word)):
            for c in list(string.ascii_lowercase):
                next_word = curr_word[:i] + c + curr_word[i + 1:]
                if next_word != curr_word and next_word in word_bag:
                    next_words.append(next_word)
        return next_words