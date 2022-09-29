# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappush(heap, n)
            heapq.heappop(heap)
        return heap[0]
        """
        if not nums: 
            return
        pivot = random.choice(nums)
        left_arr = [x for x in nums if x > pivot]
        mid_arr = [x for x in nums if x == pivot] 
        right_arr = [x for x in nums if x < pivot]
        nums = left_arr + mid_arr + right_arr
        l = len(left_arr)
        r = len(left_arr) + len(mid_arr)
        if k <= l:
            return self.findKthLargest(nums[:l], k)
        elif k > r:
            return self.findKthLargest(nums[r:], k-r)
        else:
            return nums[l]