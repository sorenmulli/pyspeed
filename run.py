#!/usr/bin/env python3
import os, sys
import torch
from argparse import ArgumentParser

from src import get_sysinfo
from src.testfuncs import retrieve_functions, run_all_tests, report_results, save_results
from src.plot import make_plots

if __name__ == '__main__':
	implementations = [
		'pure',
		'numpy',
		'torch_cpu',
		'torch_cuda',
		'cython_pure',
		'cython_c',
		'ctype_c',
		'ctype_rust',
		'numba',
	]
	cases = {
		'rootloop': [10**i for i in range(4, 10)],
	}
	disabled = {
		'torch_cuda': not torch.cuda.is_available()
	}
	for key, is_disabled in disabled.items():
		if is_disabled:
			implementations.pop(implementations.index(key))
			print("Disabling %s" % key)

	parser = ArgumentParser(description="Test speed of Python implementations on a number of code cases")
	parser.add_argument('--impl',  type=str, nargs='+', help='What implementations to test. If not given, test all')
	parser.add_argument('--cases', type=str, nargs='+', help='What cases to test. If not given, test all')
	parser.add_argument('--reps',  type=int, help='Number of repetitions for each combination (default=10)', default=10)
	parser.add_argument('--out',   type=str, help='Folder to save results (default: working dir.)', default='')
	parser.add_argument('--progress', dest='progress', action='store_true', help="Print progress and results of first function calls")
	parser.add_argument('--maxtime', type=float, help="Store measuring times when executation times exceed the given value (seconds)", default=1e9)
	parser.set_defaults(progress=False)

	args = parser.parse_args()
	if args.impl:
		implementations = args.impl
	if args.cases:
		cases = {name: cases[name] for name in args.cases}

	all_funcs = retrieve_functions( implementations, cases.keys(), os.path.join(os.path.dirname( sys.argv[0] ), 'src') )
	print(f"Starting evaluation of {len(cases)} case(s) in {len(implementations)} different implementation(s).")
	print(f"Repetitions: {args.reps}. Function calls: {len(implementations) * args.reps * sum(len(c) for c in cases.values())} (each case may test multiple arguments)")
	print()

	all_results = run_all_tests(all_funcs, cases, args.reps, args.maxtime, _print=args.progress)
	result_report = report_results(all_results, cases, args.reps)
	save_results(all_results, result_report, args.out)

	print(result_report)
	print()
	print(f"Results and report saved to {os.path.abspath(args.out)}.")
	print("Results are pickled as a dict of dicts with numpy ndarrays as values.")

	print("Making plots and saving to 'plots' folder")
	make_plots(cases, all_results, get_sysinfo())
