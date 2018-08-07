#11. 盛最多水的容器
#从两侧向中间集中，短的一端换位置，找一个数存储最大值
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res,l_tag,r_tag = 0,0,len(height)-1
        
        while l_tag<r_tag:
            if height[l_tag]>height[r_tag]:
                res = max(height[r_tag]*(r_tag-l_tag),res)
                r_tag -= 1
            else:
                res = max(height[l_tag]*(r_tag-l_tag),res)
                l_tag += 1
                
        return res
        
        
#84. 柱状图中最大的矩形        
