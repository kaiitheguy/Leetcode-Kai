# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # The min ops to make array equal is 
    # to move all elements to the median
    # So first sort the array and find the median
    # Python sort takes O(N*logN)
    A.sort()
    median = A[len(A)//2]
    # Store operations to make arr equal
    ops = 0
    # Loop the A with O(N)
    for a in A:
        ops += abs(a - median)
    # So the final complexity is O(N*logN)
    return ops
