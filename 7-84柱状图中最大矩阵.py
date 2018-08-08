#柱状图中绘制最大面积

#方法二：使用栈的思想https://blog.csdn.net/jingsuwen1/article/details/51577983
#构造升序数组比较，后一个比当前小，则代表该值的最大
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) < 1:
            return 0
        
        s = []
        result = 0
        s.append(heights[0])
        
        for i in range(1,len(heights)):
              
            count = 1
            while s and s[-1] > heights[i]:
                temp = s.pop()
                result = max(result,temp * count)
                count += 1
            #弹出多个时，需要增加多个进去    
            for j in range(count):  
                s.append(heights[i])
        
        count = 1
        while s :
            temp = s.pop()
            result = max(result,temp * count)
            count += 1
            
        return result
    
    
    
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
