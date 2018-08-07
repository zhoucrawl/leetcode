
#分治法
class Solution(object):
    def uniquePaths(self,m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 and n < 1:
            return 0
        if m==1 and n==1:
            return 1
        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

#动态规划

    
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m==1 and n==1):return 1
        if (m<1 or n<1):return -1
        
        tmp = [[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                tmp[i][j]= tmp[i-1][j]+tmp[i][j-1]
        return tmp[-1][-1]

 
#有障碍的解法  
#方法一
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] ==1:
            return 0
        if m == 0 and n == 0 :
            return -1
        
        tmp = [[0 for x in range(n)] for x in range(m)]
        
        #判断只有一行或者一列的情况
        for i in range(n):
            tmp[0][i] = 1
            if obstacleGrid[0][i] == 1:
                tmp[0][i] = 0
                break
        for i in range(m):
            tmp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                tmp[i][0] = 0
                break
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    tmp[i][j]==0
                else:
                    tmp[i][j] = tmp[i-1][j] + tmp[i][j-1]
        
        return tmp[-1][-1]
    
    #方法二：
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        P = [[0 for j in range(n+1)] for i in range(m+1)]
        
        P[0][1] = 1
        
        for i in range(1,m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] != 1:
                    P[i][j] = P[i-1][j] + P[i][j-1]
        return P[m][n]
