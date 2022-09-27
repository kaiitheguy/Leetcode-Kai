# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # Get s inside []
                temp_s = ""
                while stack[-1] != "[":
                    # Append reversely
                    temp_s = stack.pop() + temp_s
                # Remove the left bracket.
                stack.pop()
                # Get digit since it can be larger than 10
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # Append back multiplied string
                stack.append(int(k) * temp_s)
        return "".join(stack)