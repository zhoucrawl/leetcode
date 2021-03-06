
#题目：word1转化成word2的最小转化次数、可删除、增加、替换
#https://blog.csdn.net/u011521382/article/details/52034653图中矩阵规律
#单词分别建立横轴竖轴，然后依次word1单词转化word2时次数加一，相同取对角，不同时取上、左、对角的最小值

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        if m < 1:
            return n
        if n < 1:
            return m
        
        dp = [[0 for x in range(m+1)] for x in range(n+1)]
        
        for i in range(1,m+1):
            dp[0][i] = i
            
        for j in range(n+1):
            dp[j][0] = j
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]
