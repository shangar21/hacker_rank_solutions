import math

def maxSubsetSum(arr):
	
	dp = [0]*len(arr)
	dp[0] = max(0, nums[0])
	if n>1:
		dp[1] = max(0, nums[1])
	if n>2:
		dp[2] = max(dp[i-2], dp[i-2] + arr[i])
	for i in range(2,n):
		if i>= 3:
			dp[i] = max(dp[i-2], dp[i-2]+arr[i], dp[i-3], dp[i-3]+arr[i])
	return max(dp)

