
# Knapsack packing

# input: 
# weights: list of weights [w_1, ... ,w_n]
# prices: list of corresponding prices [p_1, ... ,p_n]
# backpack size B

# output: 
# optimal packing, i.e. max sum p_i, i in I s.t. sum w_i <= B, i in I. 

def knapsack(weights,prices,B):
    assert isinstance(weights, list),TypeError
    assert all(isinstance(weight,int) and weight>0 for weight in weights), "Input weights must be positive integers."
    assert isinstance(prices, list),TypeError
    assert all(isinstance(price,int) and price>0 for price in prices), "Input prices must be positive integers."
    assert len(weights)==len(prices), "Input for weights and prices have different lengths."
    assert isinstance(B,int) and B>0, "The budget B must be a positive integer."
    
    n=len(weights)
    prices_sum=sum(prices)

    # min_weight[i][p] is the minimal weight of a packing I subset {1,...,i} of the first 1,...,i items such the price of the packing is p.
    # optimal_packing[i][p] is an optimal packing I subset {0,...,i-1} of the first 0,...,i-1 item indices such the price of the packing is p.
    min_weight=[[float("inf") for _ in range(prices_sum+1)] for _ in range(n+1)] # we want to also capture the cases i==0 and p==0 for min_weight[i][p].
    for i in range(n+1):
        min_weight[i][0]=0
    optimal_packing=[[set() for _ in range(prices_sum+1)] for _ in range(n+1)]

    for i in range(n): # i is the index and not the item.
        for p in range(prices_sum+1):
            if p-prices[i]>=0 and min_weight[i][p-prices[i]]+weights[i]<min_weight[i][p]:
                optimal_packing[i+1][p]=optimal_packing[i][p-prices[i]].union({i})
                min_weight[i+1][p]=min_weight[i][p-prices[i]]+weights[i]
            else:
                optimal_packing[i+1][p]=optimal_packing[i][p]
                min_weight[i+1][p]=min_weight[i][p]

    for p in range(prices_sum,-1,-1):
        if min_weight[n][p]!=set() and min_weight[n][p]<=B:
            return optimal_packing[n][p]


"""
print(knapsack([1,2],[2,1],2))
print(knapsack([1,2],[1,2],2)) 
print(knapsack([2,3,4,5],[3,4,5,8],5)) 
print(knapsack([1,2,3,5],[1,6,10,16],8)) # sol: item 3 (weight 3, value 10) and item 4 (weight 5, value 16), for a total value of 26 and a total weight of 8
print(knapsack([1,2,3,5],[1,6,10,14],6))# sol: item 2 (weight 2, value 6) and item 3 (weight 3, value 10) and item 1 (weight 1, value 1)
print(knapsack([1,2,3,5],[1,6,10,20],6))
"""