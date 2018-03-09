题目大意：从最顶端往下走，寻找和最小的路径。
显然，从最顶端往下走有很多条路径可以走，但是每一条路径的sum不一样，题目要求sum最小，属于最优化问题，考虑动态规划。

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 
        res=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j]=min(res[j],res[j+1])+triangle[i][j]
        return res[0]
