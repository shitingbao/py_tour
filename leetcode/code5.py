#!/usr/bin/python3
class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        resList = [0] * (len(arr) + 1)
        for i in range(1, len(arr)+1):
            maxNum = arr[i-1]
            for idx in range(i-1, max(-1, i-k-1), -1):
                resList[i] = max(resList[i], resList[idx]+maxNum*(i-idx))
                if idx > 0 and arr[idx-1] > maxNum:
                    maxNum = arr[idx-1]
        return resList[len(arr)]


su = Solution()
max = su.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)
# max = su.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4)
print(max)
