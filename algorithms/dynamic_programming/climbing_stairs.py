"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"
"""

def climbStairs(n: int) -> int:
        
    dp=[0]*(n+1)

    for i in range(n+1):
        if i==0 or i==1:
            dp[i]=1
        elif i==2:
            dp[i]=2
        else:
            dp[i]=dp[i-2]*2+dp[i-3]

    return dp[n]

#print(climbStairs(3))