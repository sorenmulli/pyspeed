import torch
def rootloop(N):
	# Coerce to float as pyTorch has not defined square root for ints
	return torch.sum( torch.sqrt( torch.arange(0.0, N, 2, device=torch.device('cpu')) ) )
