# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

    def __init__(self):
        self.rootNode = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        currentPointer = self.rootNode
        for character in word:
            index = (ord(character) - ord("a"))
            if currentPointer.children[index] == None:
                currentPointer.children[index] = TrieNode()
            currentPointer = currentPointer.children[index]
        currentPointer.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        currentPointer = self.rootNode
        for character in word:
            index = (ord(character) - ord("a"))
            if currentPointer.children[index] == None:
                return False
            currentPointer = currentPointer.children[index]
        if currentPointer.end == True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        currentPointer = self.rootNode
        for character in prefix:
            index = (ord(character) - ord("a"))
            if currentPointer.children[index] == None:
                return False
            currentPointer = currentPointer.children[index]
        return True

        
class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)