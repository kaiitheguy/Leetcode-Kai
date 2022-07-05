# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)
        """
        counter = collections.Counter(s)
        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
        for c in counter.values():
            if c != 0:
                return False
        return True
        """