class Solution(object):
    def quickSort(self, arr, left, right):
        if left < right:
            pi = self.partition(arr, left, right)
            print(arr)
            self.quickSort(arr, left, pi - 1)
            self.quickSort(arr, pi, right)

    def partition(self, arr, left, right):
        pivot = right
        j = left - 1
        for i in range(left, right):
            if arr[i] < arr[pivot]:
                j += 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        j += 1
        (arr[pivot], arr[j]) = (arr[j], arr[pivot])
        return j

arr = [8, 7, 2, 1, 0, 9, 6]
Solution().quickSort(arr, 0, len(arr) - 1)
print(arr)