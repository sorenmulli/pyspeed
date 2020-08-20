def rootloop(N):
	x = 0
	for i in range(0, N, 2):
		x += i ** (.5)
	return x
