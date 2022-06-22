# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # If the N is even
    # The array would be like [-N//2, ..., -1, 1, ..., N//2]
    # And I will construct the array by two parts since 0 needs to be skipped
    if N % 2 == 0:
        return [n for n in range(-N//2, 0)] + [n for n in range(1, N//2 + 1)]
    # Else if N is odd
    # The array would be like [-N//2 + 1, ..., -1, 0, 1, ..., N//2 - 1]
    else:
        return [n for n in range(-N//2 + 1, 1)] + [n for n in range(1, N//2 + 1)]
    # This solution take O(N)
    # The construction of two arrays takes N/2 each and adds up to O(N)