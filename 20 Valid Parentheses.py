# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        stack = []
        dic = dict(zip(right, left))
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if dic[c] != stack.pop():
                    return False
        return len(stack) == 0