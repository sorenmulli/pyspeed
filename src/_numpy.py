import numpy as np

def rootloop(N):
	return np.sum( np.sqrt( np.arange(0, N, 2, dtype=int) ) )
