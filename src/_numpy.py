import numpy as np

def rootloop(N):
	# Use float to be comparable with pyTorch
	return np.sum( np.sqrt( np.arange(0.0, N, 2) ) )
