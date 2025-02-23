"""
Mock Interview 5 -
You have been given infinite coins of denomination 1,2,6
You have 2 coins of denomination 4
amount = 6
Find number of ways to form the amount

DP approach-
TC - O(m * n)
SC - O(m * n)
"""


def calcWays(coins, amt):
    if coins is None or len(coins) == 0 or amt is None: return 0

    m = len(coins)+1
    n = amt + 1

    dp = [[0 for i in range(n)] for i in range(m)]
    # print(dp)

    # fill 1st col with 1
    for i in range(m):
        dp[i][0] = 1

    # print(dp)

    for i in range(1, m):
        coin = coins[i - 1]
        for j in range(1, n):
            if coin == 4:
                dp[i][j] = 0
                for k in range(3):  # k = 0, 1, 2
                    if j - k * coin >= 0:
                        dp[i][j] += dp[i - 1][j - k * coin]
            else:
                if j < coin:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coin]

    # print(dp)
    return dp[m-1][n-1]


if __name__ == '__main__':
    coins = [1, 2, 4, 6]
    amount = 6
    print(calcWays(coins, amount))
