# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        word = []
        for i in s:
            if  i.isalnum()==True:
                word.append(i) 
        return (word==list(reversed(word)))