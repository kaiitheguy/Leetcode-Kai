# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from collections import defaultdict

class TrieNode(object):
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
    
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr_node = self.root
        for w in word:
            curr_node = curr_node.children[w]
        curr_node.end = True
            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, self.root)
        
    def searchHelper(self, word, node):
        res = False
        if len(word) == 0:
            #if word[0] == "." or word[0] in node.children.keys():
            if node.end == True:
                res = True
            else:
                res = False
        else:
            if word[0] == ".":
                for key in node.children.keys():
                    res = res or self.searchHelper(word[1:], node.children[key])
            else:
                if word[0] in node.children.keys():
                    res = self.searchHelper(word[1:], node.children[word[0]])
                else:
                    res = False
        return res
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)