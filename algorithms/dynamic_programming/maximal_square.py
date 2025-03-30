"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""


def maximalSquare(matrix: list[list[str]]) -> int:
    
    m=len(matrix)
    n=len(matrix[0])

    res=0

    # we use dynamic programming. We initalize any matrix of the same size as matrix. Let us choose the zero matrix and call it dp. 
    # dp[i][j] determines the size (side length) of a maximal square of 1's with lower right corner at coordinate i,j. 
    # The lower right corner is purposely chosen so that we get the fresh updates if we loop the matrix from top to bottom and left to right. 
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=="1":
                if i==0 or j==0:
                    dp[i][j]=1
                    if res<1:
                        res=1
                else:
                    # update by looking at the upper left 3 squares around the lower right corner and adding 1 to the side length of the maximal square.
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    if res<dp[i][j]**2:
                        res=dp[i][j]**2
    return res


#print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))