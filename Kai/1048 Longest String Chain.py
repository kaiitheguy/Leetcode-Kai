# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        visited = set()
        self.longest_count = 0
        
        def dfs(word, count):
            self.longest_count = max(self.longest_count, count)
            for i in range(len(word)):
                if i == len(word)-1:
                    new_word = word[:-1]
                else:
                    new_word = word[:i] + word[i+1:]
                if new_word in words_set and new_word not in visited:
                    visited.add(new_word)
                    dfs(new_word, count+1)
                
        words.sort(key = lambda x:len(x), reverse = True)
        for word in words:
            if word not in visited:
                dfs(word, 1)
        return self.longest_count