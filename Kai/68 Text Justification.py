# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        stack = []
        curr_width = 0
        i = 0
        res = []
        while i < len(words):
            word = words[i]
            length = len(word)
            if curr_width + length <= maxWidth:
                stack.append(word)
                curr_width += length + 1
                i += 1
            else:
                total_space = maxWidth - curr_width + len(stack)
                if len(stack) == 1:
                    temp_str = ""
                    temp_str += stack[0]
                    for j in range(total_space):
                        temp_str += " "
                    res.append(temp_str)
                    stack = []
                    curr_width = 0
                else:
                    avg = total_space // (len(stack) - 1)
                    left = total_space % (len(stack) - 1)
                    temp_str = ""
                    for j in range(len(stack)-1):
                        temp_str += stack[j]
                        for k in range(avg):
                            temp_str += " "
                        if left > 0:
                            temp_str += " "
                            left -= 1
                    temp_str += stack[-1]
                    res.append(temp_str)
                    stack = []
                    curr_width = 0
        if stack:
            total_space = maxWidth - curr_width + len(stack)
            if len(stack) == 1:
                temp_str = ""
                temp_str += stack[0]
                for j in range(total_space):
                    temp_str += " "
                res.append(temp_str)
                stack = []
                curr_width = 0
            else:
                temp_str = ""
                for j in range(len(stack)-1):
                    temp_str += stack[j]
                    temp_str += " "
                temp_str += stack[-1]
                for j in range(total_space-len(stack)+1):
                    temp_str += " "
                res.append(temp_str)
        return res