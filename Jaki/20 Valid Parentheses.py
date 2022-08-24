# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        check = {"(":0,"{":0,"[":0}
        for i in s:
            if i in check.keys():
                check[i] += 1
            else:
                if i==")":
                    check["("]-=1
                    if check["("]<0:
                        return False
                elif i=="}":
                    check["{"]-=1
                    if check["{"]<0:
                        return False
                else:
                    check["["]-=1
                    if check["["]<0:
                        return False
        return True
        """ 
        left = []
        right = []
        for i in s:
            if i in ["(","[","{"]:
                left.append(i)
            else:
                if len(left)==0:
                    return False
                left_item = left.pop()
                if i=="}" and left_item!="{":
                    return False
                elif i==")" and left_item!="(":
                    return False
                elif i=="]" and left_item!="[":
                    return False
        if len(left)==0:
            return True
        else:
            return False