import torch
def rootloop(N):
	# Coerce to double as pyTorch defaults to float32 otherwise
	return torch.sum( torch.sqrt( torch.arange(0, N, 2, device=torch.device('cpu'), dtype=torch.double) ) )
