# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        check1 = {}
        check2 = {}
        for i in s:
            if i in check1.keys():
                check1[i]+=1
            else:
                check1[i]=1
        for i in t:
            if i in check2.keys():
                check2[i]+=1
            else:
                check2[i]=1
        return (check1==check2)
        """
        check1 = collections.defaultdict(int)
        check2 = collections.defaultdict(int)
        for i in s:
            check1[i]+=1
        for i in t:
            check2[i]+=1
        return (check1==check2)