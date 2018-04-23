
利用列表自身的属性，如果倒叙输出是否和正序一致
def isPalindrome2(s):
    return s == s[::-1]
    
利用递归

def is_huiwen(s):
    if len(s)<=1:
        return True
    
    else:
        return s[0]==s[-1] and is_huiwen(s[1:-1])
        
        
题目大意：给定一个字符串，返回最小的切割数，使得切割后形成的所有字符串都是回文的。
我们知道，对于一个长度为n的字符串，它里面可以切割的位置有n-1个，
每个位置可切割可不切割，这样一共会产生2^(n-1)种方案，我们的任务就是从所有方案中，

找出满足以下两个条件的那个方案：1、切割后形成的所有字符串都是回文的。2、符合条件1的所有方案中切割数最小。

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        
        
        for i in range(1,len(s)):
            if s[:i]==s[:i][::-1] and s[i:]==s[i:][::-1]:
                return 1
            
        cut = [x for x in range(-1,len(s))]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]
