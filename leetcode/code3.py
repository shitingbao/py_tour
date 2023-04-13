class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        for num in nums:
            if num%2 !=0:
                continue
            if num not in numMap:
                numMap[num] = 1
                continue
            numMap[num] = numMap[num]+1
        if len(numMap) == 0:
            return -1
        max = 0
        key = 0
        flag = True
        for k,v in numMap.items():
            if flag:
                max = v
                key = k
                flag = False
                continue
            if v>max:
                max = v
                key = k
            if v==max and k<key:
                max = v
                key = k
        return key
    
solu = Solution()
print(solu.mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
