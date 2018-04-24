
int uniquePaths(int m, int n) {  
        if(m<1 or n<1) return 0;  
        if(m==1 and n==1) return 1;  
        return uniquePaths(m-1,n)+uniquePaths(m,n-1);  
    } 
class Solution:    
    def uniquePaths(int m,intn):
        if (m<1 or n<1): return 0
        if (m==1 and n==1):return 1
        return uniquepPaths(m-1,n)+uniquePaths(m,n-1);
