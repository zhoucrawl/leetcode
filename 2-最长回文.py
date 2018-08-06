'''
题目大意：
返回字符串S的最长回文

解析思路：
1.特殊情况考虑，只有一个或者全部是回文
2.找出最长回文的maxlen，依次寻找迭代
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1 or s==s[::-1]:
          return s
        
        start,maxlen = 0,1
        for idx in range(1,len(s)):
          add2 = s[idx-maxlen-1:idx+1]
          if idx-maxlen-1>=0 and add2 == [add2::-1]:
            start = idx-maxlen-1
            maxlen += 2
            continue
          
          add1 = s[idx-maxlen:idx+1]
          if add1 == [add1::-1]:
            start = idx-maxlen
            maxlen+=1
        
        return s[start:(start+maxlen)]
          
