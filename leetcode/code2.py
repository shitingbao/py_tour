class Solution:
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        list = {}
        for point in points:
            list[point[0]] = True
        
        queue = []
        for key in list:
            queue.append(key)
        queue.sort()
        max = 0
        for idx in range(len(queue)):
            if idx==0:
                continue
            num = queue[idx] - queue[idx-1]
            if num > max:
                max = num
        return max

su = Solution()
max = su.maxWidthOfVerticalArea([[1,2],[2,3],[34,42],[562,83],[71,452],[672,374]])
print("max:",max)