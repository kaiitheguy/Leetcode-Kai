# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Not the same

"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 0 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to sub 1 to it.

It is guaranteed that you can always reach one for all test cases.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    # Store operations needed
    ops = 0
    had_one = False
    # The regular solution can not pass time complextity test
    # Thus use bit solution of O(N)
    # Divide by 2 is the same as >> 1
    # 1100 / 2 == 1100 >> 1 == 110
    for i in range(len(S)-1, -1, -1):
        # If a digit is 0, then right shift one thus ops += 1
        if S[i] == '0':
            # If the left most digit is 0, nothing needs to be done
            if i != len(S) - 1:
                ops += 1
        # If a digit is 1, then sub by 1 and do one right shift
        # Thus ops += 2
        else:
            ops += 2
            had_one = True
    # The left most 1 will count one more ops
    # So sub 1 if "1" occurs
    if had_one:
        return ops - 1
    else:
        return ops