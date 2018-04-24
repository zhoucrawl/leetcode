
#分治法
class Solution:    
    def uniquePaths(int m,intn):
        if (m<1 or n<1): return 0
        if (m==1 and n==1):return 1
        return uniquepPaths(m-1,n)+uniquePaths(m,n-1);

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
