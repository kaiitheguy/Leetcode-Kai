# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        digits_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        
        def backtrack(i, j, tmp):
            if i >= len(digits):
                res.append("".join(tmp))
                return
            if j >= len(digits_dict[digits[i]]):
                return 
            tmp.append(digits_dict[digits[i]][j])
            backtrack(i+1, 0, tmp)
            tmp.pop()
            backtrack(i, j+1, tmp)
            
        backtrack(0, 0, [])
        
        return res