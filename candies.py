def candies(n, arr):
    dp = [1]*n

    for i in range(n-1):
        if arr[i+1] > arr[i]:
            dp[i+1] += dp[i]

    for i in range(n-1,0,-1):
        if arr[i-1] > arr[i] and dp[i-1] <= dp[i]:
            dp[i-1] += dp[i]

    return sum(dp)


candies(5,[1,1,1,1,1])