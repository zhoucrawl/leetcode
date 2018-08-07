
#1.给定一个数组，找出连续子串的最大值。
#方法一，没有使用内置函数，减少了时间

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        sum = 0
        
        for idx in range(len(nums)):
            if sum < 0:
                sum = 0  
            #每次加的为大于等于0的数    
            sum += nums[idx]
            if max < sum:
                max = sum
                
        return max


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
