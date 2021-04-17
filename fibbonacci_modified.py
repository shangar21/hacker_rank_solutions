def fibonacciModified(t1,t2,n):

	dp = [0]*n
	dp[0], dp[1] = t1, t2

	for i in range(2, n):
		dp[i] = dp[i-2] + (dp[i-1]**2)

	return dp[-1]


