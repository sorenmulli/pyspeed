def loops(N):
	a = 0
	for i in range(N):
		for j in range(N):
			a += (i + j)
	return a
