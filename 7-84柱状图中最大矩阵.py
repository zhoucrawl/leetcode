#柱状图中绘制最大面积

#方法一：每个柱子依次向左右计算，比它大就加。
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) < 1:
            return 0
        
        area = 0
        tag = 0
        for i in range(len(heights)):
            area,curarea = heights[i],heights[i]
          
            for j in range(i+1,len(heights)):
                if heights[j] >= heights[i]:
                    area += curarea
                else:
                    break
            for j in range(i-1,-1,-1):
                if heights[j] >= heights[i]:
                    area += curarea
                else:
                    break
           
            if area >= tag:
                tag = area
        
        return tag
