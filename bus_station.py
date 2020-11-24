def solve(a):
    bus = []
    total = sum(a)
    for i in range(max(a), total+1):
    	if total % i == 0:
        	bus.append(i)
    return bus


print(solve([1,2,1,1,1,2,1,3]))