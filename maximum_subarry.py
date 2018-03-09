
1.给定一个数组，找出连续子串的最大值。

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        
        max_sub,fn=nums[0],0
        
        for value in nums:
            fn = max(value,fn+value)         #计算当前值，当前值的大小和之前的值累加相比较
            max_sub = max(max_sub,fn)        #当前子串的值，与加上当前子串的值，或者新建一个子串
        return max_sub
