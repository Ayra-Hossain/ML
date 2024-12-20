import sys
def mcm(p, i, j):

	if i == j:
		return 0

	min = sys.maxsize

	for k in range(i, j):

		count = (mcm(p, i, k)
			+ mcm(p, k + 1, j)
				+ p[i-1] * p[k] * p[j])

		if count < min:
			min = count;

	return min;

arr = [5, 7, 3, 7, 11, 5];
n = len(arr);

print("Minimum number of multiplications is ", mcm(arr, 1, n-1));
